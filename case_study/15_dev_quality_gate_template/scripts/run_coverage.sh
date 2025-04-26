#!/bin/bash

# set -euo pipefail

REQUIRED_COVERAGE=80

# ANSI Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

print() {
    echo -e "$@"
}

run_tests_with_coverage() {
    print "${YELLOW}Running tests with coverage...${NC}"

    # Run tests with short traceback and verbose output
    coverage_output=$(coverage run -m pytest -v --tb=short 2>&1)
    test_exit_code=$?

    echo "$coverage_output"

    if [ $test_exit_code -ne 0 ]; then
        print "\n${RED}Some tests failed. Summary of failures:${NC}"

        # Extract test failure summaries from pytest output
        echo "$coverage_output" | awk '
            /^FAILED/ {
                print "🔻 " $0
            }
            /^\s*tests\// && /AssertionError/ {
                print "   🔹 " $0
            }
        '

        print "\n${RED}Push blocked due to test failures. Please fix them.${NC}"
        exit 1
    fi
}


check_coverage() {
    coverage_report=$(coverage report 2>&1 || true)
    # echo "$coverage_report"
    if ! echo "$coverage_report" | grep -q 'TOTAL'; then
        print "${RED} Failed to parse coverage report.${NC}"
        echo "$coverage_report"
        exit 1
    fi

    coverage_percent=$(echo "$coverage_report" | grep TOTAL | awk '{print $6}' | sed 's/%//')

    print "\nTotal coverage: $coverage_percent%"

    if (( $(echo "$coverage_percent < $REQUIRED_COVERAGE" | bc -l) )); then
        print "${RED}Test coverage too low: $coverage_percent% (required: ${REQUIRED_COVERAGE}%)${NC}"
        exit 1
    else
        print "${GREEN}Test coverage OK: $coverage_percent%${NC}"
    fi
}

main() {
    run_tests_with_coverage
    check_coverage
}

main "$@"
