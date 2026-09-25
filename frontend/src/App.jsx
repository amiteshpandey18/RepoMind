import { useState } from "react";
import ReactMarkdown from "react-markdown";

import Login from "./pages/Login";
import Register from "./pages/Register";
import Repository from "./pages/Repository";

import "./App.css";


function App() {

  const [page, setPage] = useState("login");

  const [loggedIn, setLoggedIn] = useState(
    Boolean(localStorage.getItem("access_token"))
  );

  const [repositoryConnected, setRepositoryConnected] = useState(
    Boolean(localStorage.getItem("repository_owner"))
  );


  if (!loggedIn) {

    if (page === "register") {

      return (
        <Register
          onShowLogin={() => setPage("login")}
        />
      );

    }

    return (
      <Login
        onLogin={() => setLoggedIn(true)}
        onShowRegister={() => setPage("register")}
      />
    );

  }


  if (!repositoryConnected) {

    return (
      <Repository
        onRepositoryConnected={() =>
          setRepositoryConnected(true)
        }
      />
    );

  }


  return (
    <Chat />
  );
}


function Chat() {

  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);


  const logout = () => {

    localStorage.removeItem("access_token");
    localStorage.removeItem("repository_owner");
    localStorage.removeItem("repository_name");

    window.location.reload();

  };


  const askQuestion = async () => {

    if (!question.trim() || loading) {
      return;
    }

    const currentQuestion = question;

    const owner = localStorage.getItem(
      "repository_owner"
    );

    const repo = localStorage.getItem(
      "repository_name"
    );


    setMessages((previousMessages) => [
      ...previousMessages,
      {
        role: "user",
        content: currentQuestion
      },
      {
        role: "assistant",
        content: ""
      }
    ]);

    setQuestion("");
    setLoading(true);


    try {

      const response = await fetch(
        "http://127.0.0.1:8000/agent/stream",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization":
              `Bearer ${localStorage.getItem("access_token")}`
          },
          body: JSON.stringify({
            question: currentQuestion,
            owner: owner,
            repo: repo,
            thread_id: "repo-1"
          })
        }
      );


      if (!response.ok) {
        throw new Error("Failed to get response");
      }


      if (!response.body) {
        throw new Error("Streaming is not supported");
      }


      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      let answer = "";


      while (true) {

        const { value, done } = await reader.read();

        if (done) {
          break;
        }


        const chunk = decoder.decode(value, {
          stream: true
        });

        answer += chunk;


        setMessages((previousMessages) => {

          const updatedMessages = [...previousMessages];

          updatedMessages[updatedMessages.length - 1] = {
            role: "assistant",
            content: answer
          };

          return updatedMessages;

        });

      }


    } catch (error) {

      console.error(error);

      setMessages((previousMessages) => {

        const updatedMessages = [...previousMessages];

        updatedMessages[updatedMessages.length - 1] = {
          role: "assistant",
          content: "Something went wrong. Please try again."
        };

        return updatedMessages;

      });

    } finally {

      setLoading(false);

    }
  };


  return (
    <div className="app">

      <header className="header">

        <div>
          <h1>RepoMind</h1>
          <p>AI assistant for your GitHub repository</p>
        </div>


        <div className="header-right">

          <div className="status">
            <span></span>
            Connected
          </div>


          <button
            className="logout-button"
            onClick={logout}
          >
            Logout
          </button>

        </div>

      </header>


      <main className="chat-container">

        <div className="chat-header">

          <div>
            <h2>Repository Assistant</h2>
            <p>Ask questions about your codebase</p>
          </div>

        </div>


        <div className="messages">

          {messages.length === 0 && (

            <div className="welcome">

              <div className="welcome-icon">
                🤖
              </div>

              <h2>How can I help?</h2>

              <p>
                Ask RepoMind about your repository,
                authentication, APIs, commits, issues,
                pull requests, or implementation details.
              </p>


              <div className="suggestions">

                <button
                  onClick={() =>
                    setQuestion(
                      "What authentication does this project use?"
                    )
                  }
                >
                  What authentication does this project use?
                </button>


                <button
                  onClick={() =>
                    setQuestion(
                      "Show me the recent commits"
                    )
                  }
                >
                  Show me the recent commits
                </button>


                <button
                  onClick={() =>
                    setQuestion(
                      "Are there any open issues?"
                    )
                  }
                >
                  Are there any open issues?
                </button>

              </div>

            </div>

          )}


          {messages.map((message, index) => (

            <div
              key={index}
              className={`message-row ${message.role}`}
            >

              <div className="avatar">
                {message.role === "user" ? "You" : "AI"}
              </div>


              <div className="message">

                <div className="message-name">
                  {message.role === "user"
                    ? "You"
                    : "RepoMind"}
                </div>


                <div className="message-content">

                  {message.role === "assistant" ? (
                    <ReactMarkdown>
                      {message.content}
                    </ReactMarkdown>
                  ) : (
                    message.content
                  )}

                </div>

              </div>

            </div>

          ))}

        </div>


        <div className="input-area">

          <div className="input-wrapper">

            <input
              type="text"
              value={question}
              onChange={(event) =>
                setQuestion(event.target.value)
              }
              onKeyDown={(event) => {

                if (
                  event.key === "Enter" &&
                  !event.shiftKey
                ) {
                  event.preventDefault();
                  askQuestion();
                }

              }}
              placeholder="Ask RepoMind about your repository..."
              disabled={loading}
            />


            <button
              onClick={askQuestion}
              disabled={loading || !question.trim()}
            >
              {loading ? "..." : "Send"}
            </button>

          </div>


          <p className="input-hint">
            Press Enter to send
          </p>

        </div>

      </main>


      <footer>
        RepoMind • AI-powered GitHub repository assistant
      </footer>

    </div>
  );
}


export default App;