import React, { useEffect, useState } from "react";
import useSpeechToText from "react-hook-speech-to-text";
import { useSpeech } from "react-text-to-speech";
import axios from "axios";
import { ThreeDots } from "react-loader-spinner";

const Form = () => {
  const [query, setQuery] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [responseText, setResponseText] = useState("");
  const [questions, setQuestions] = useState([]);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [score, setScore] = useState(0);
  const [submitted, setSubmitted] = useState(false);

  const voices = [
    { name: "Google UK English Female" },
    { name: "Google UK English Male" },
  ];

  const [selectedVoice, setSelectedVoice] = useState(voices[0].name);

  // Speech settings
  const { speechStatus, start, pause, stop } = useSpeech({
    text: responseText,
    pitch: 1,
    rate: 1,
    volume: 1,
    voiceURI: selectedVoice,
    autoPlay: true,
  });

  const handleSubmit = async () => {
    if (!query.trim()) return;

    setIsLoading(true);
    setQuestions([]); // Clear previous questions
    setResponseText(""); // Clear previous response

    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/tutor/query?question=${encodeURIComponent(query)}`
      );

      console.log("Full Response:", response.data);
      setResponseText(response.data);
      start();

      // Try to extract MCQs from response
      try {
        const jsonMatch = response.data.match(/\[.*\]/s);
        if (jsonMatch) {
          let data = jsonMatch[0]
            .replace(/'/g, '"') // Fix single quotes
            .replace(/,(\s*[}\]])/g, '$1') // Remove trailing commas
            .trim();

          const parsedData = JSON.parse(data);

          if (Array.isArray(parsedData)) {
            setQuestions(parsedData);
          } else if (Array.isArray(parsedData.questions)) {
            setQuestions(parsedData.questions);
          }
        }
      } catch (error) {
        console.error("Error parsing JSON:", error);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // Speech-to-text handling
  const {
    error,
    interimResult,
    isRecording,
    startSpeechToText,
    stopSpeechToText,
  } = useSpeechToText({
    continuous: true,
    useLegacyResults: false,
  });

  useEffect(() => {
    if (interimResult) {
      setQuery(interimResult);
    }
  }, [interimResult]);

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleButtonClick = () => {
    if (isRecording) {
      stopSpeechToText();
      handleSubmit();
    } else if (query.trim()) {
      handleSubmit();
    } else {
      startSpeechToText();
    }
  };

  // Handle option selection
  const handleOptionChange = (questionId, selectedOption) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [questionId]: selectedOption,
    }));
  };

  // Submit MCQ answers
  const handleMCQSubmit = () => {
    let newScore = 0;
    questions.forEach((q) => {
      if (selectedAnswers[q.id] === q.correct_answer) {
        newScore++;
      }
    });
    setScore(newScore);
    setSubmitted(true);
  };

  if (error) {
    return <p>Web Speech API is not available in this browser 🤷‍♂️</p>;
  }

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      {/* Query Form */}
      <form onSubmit={(e) => e.preventDefault()}>
        <div style={{ marginBottom: "10px" }}>
          <label>Question:</label>
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            required
            style={{
              padding: "8px",
              width: "80%",
              marginRight: "10px",
            }}
          />
          <button type="button" onClick={handleButtonClick}>
            {isRecording
              ? "Stop & Submit"
              : query
              ? "Submit"
              : "Start Recording"}
          </button>
        </div>

        {/* Voice Selection */}
        <div style={{ marginBottom: "10px" }}>
          <label>Select Voice:</label>
          <select
            value={selectedVoice}
            onChange={(e) => setSelectedVoice(e.target.value)}
          >
            {voices.map((voice) => (
              <option key={voice.name} value={voice.name}>
                {voice.name}
              </option>
            ))}
          </select>
        </div>
      </form>

      {/* Response */}
      {isLoading ? (
        <ThreeDots height="40" width="40" color="#4fa94d" />
      ) : (
        <p>{responseText}</p>
      )}

      {/* Speech Controls */}
      {/* {responseText && (
        <div style={{ marginTop: "10px" }}>
          <button disabled={speechStatus === "started"} onClick={start}>
            Start
          </button>
          <button disabled={speechStatus === "paused"} onClick={pause}>
            Pause
          </button>
          <button disabled={speechStatus === "stopped"} onClick={stop}>
            Stop
          </button>
        </div>
      )} */}

      {/* MCQ Section */}
      
    </div>
  );
};

export default Form;
