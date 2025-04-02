import React, { useEffect, useState } from "react";
import { useSpeech } from "react-text-to-speech";
import axios from "axios";
import {toast, ToastContainer} from "react-toastify";

import { ThreeDots } from "react-loader-spinner";

const Quiz = () => {
  const [query, setQuery] = useState("");
  const [quesNo, setQuesNo] = useState(5);
  const [isLoading, setIsLoading] = useState(false);
  const [responseText, setResponseText] = useState("");
  const [questions, setQuestions] = useState([]);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [score, setScore] = useState(0);
  const [submitted, setSubmitted] = useState(false);



  const handleOptionChange = (questionId, option) => {
    setSelectedAnswers((prev) => ({
      ...prev,
      [questionId]: option,
    }));
  };

  const handleSubmit = async () => {
    if (!query.trim()) return;
  
    setIsLoading(true);
    setQuestions([]);
    setResponseText("");
  
    try {
      const response = await axios.post(
        `http://127.0.0.1:8000/tutor/quiz?question=${encodeURIComponent(query)}&number=${quesNo}`
      );
  
  
      try {
        const jsonMatch = response.data.match(/\[.*\]/s);
        if (jsonMatch) {
        let data = jsonMatch[0];
  
          console.log("Sanitized Data:", data);
  
          try {
           let parsedData = JSON.parse(data)
          setResponseText(data);
            
            if (Array.isArray(parsedData)) {
              setQuestions(parsedData);
            } else if (Array.isArray(parsedData.questions)) {
              setQuestions(parsedData.questions);
            }
          } catch (error) {
            console.error("Error parsing JSON:", error);
            console.log("Sanitized Data from error:", data);
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
  

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      handleSubmit();
    }
  };

  const handleButtonClick = () => {
    handleSubmit();
  };

  const handleMCQSubmit = () => {
    // Ensure every question has an answer selected
    if (questions.some(q => !selectedAnswers[q.id])) {
      alert("Please answer all questions before submitting.");
      return;
    }
  
    let newScore = 0;
    questions.forEach((q) => {
      if (selectedAnswers[q.id] === q.correct_answer) {
        newScore++;
      }
    });
    setScore(newScore);
    setSubmitted(true);
  };
  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <form onSubmit={(e) => e.preventDefault()}>
        <div style={{ marginBottom: "10px" }}>
          <label>Enter Topic:</label>
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
          <label>Number of Ques:</label>
          <input
            type="number"
            value={quesNo}
            onChange={(e) => setQuesNo(e.target.value)}
            onKeyDown={handleKeyDown}
            required
            style={{
              padding: "8px",
              width: "80%",
              marginRight: "10px",
            }}
          />
          <button
            type="button"
            onClick={handleButtonClick}
            disabled={isLoading}
            style={{
              padding: "8px",
              backgroundColor: isLoading ? "#ccc" : "#4caf50",
              color: "white",
              cursor: isLoading ? "not-allowed" : "pointer",
            }}
          >
            {isLoading ? "Loading..." : "Submit"}
          </button>
        </div>
      </form>

      {isLoading ? (
        <ThreeDots height="40" width="40" color="#4fa94d" />
      ) : (
        <div>
            {questions.length > 0 && (
        <div>
          <h2>MCQs:</h2>
          {questions.map((q, c) => (
            <div key={q.id}>
              <h3>{c+1}. {q.question}</h3>
              {q.options.map((option, index) => (
                <button
                  key={index}
                  style={{
                    padding: "5px",
                    marginRight: "5px",
                    backgroundColor:
                      selectedAnswers[q.id] === option ? "#4caf50" : "indigo",
                    color: "white",
                    border: "none",
                    cursor: "pointer",
                  }}
                  onClick={() => handleOptionChange(q.id, option)}
                >
                  {option}
                </button>
              ))}
            </div>
          ))}

          <button
            onClick={handleMCQSubmit}
            style={{
              marginTop: "10px",
              padding: "8px",
              backgroundColor: "#4caf50",
              color: "white",
              cursor: "pointer",
            }}
          >
            Submit Answers
          </button>

          {submitted && <p>Your score: {score}/{questions.length}</p>}
        </div>
      )}
        </div>
      )}

<ToastContainer />
    </div>
  );
};

export default Quiz;
