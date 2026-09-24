import { useState } from "react";

function App() {
  const [isLogin, setIsLogin] = useState(true);

  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [message, setMessage] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();

    if (isLogin) {
      // Login
      const response = await fetch(
        "http://127.0.0.1:8000/auth/login",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            password: password,
          }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        localStorage.setItem(
          "access_token",
          data.access_token
        );

        setMessage("Login successful!");
      } else {
        setMessage(data.detail || "Login failed");
      }
    } else {
      // Register
      const response = await fetch(
        "http://127.0.0.1:8000/auth/register",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username,
            email: email,
            password: password,
          }),
        }
      );

      const data = await response.json();

      if (response.ok) {
        setMessage("Registration successful!");
        setIsLogin(true);
      } else {
        setMessage(data.detail || "Registration failed");
      }
    }
  }

async function getMyProfile() {
  console.log("Check Authentication clicked");

  setMessage("Button is working");

  const token = localStorage.getItem("access_token");

  console.log("Token:", token);

  if (!token) {
    setMessage("No token found. Please login first.");
    return;
  }

  setMessage("Token found. Calling backend...");

  const response = await fetch(
    "http://127.0.0.1:8000/auth/me",
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  console.log("Status:", response.status);

  const data = await response.json();

  console.log("Data:", data);

  setMessage(JSON.stringify(data));
}

  return (
    <div>
      <h1>RepoMind</h1>

      <h2>
        {isLogin ? "Login" : "Register"}
      </h2>

      <form onSubmit={handleSubmit}>

        {!isLogin && (
          <div>
            <label>Username</label>
            <br />

            <input
              type="text"
              value={username}
              onChange={(event) =>
                setUsername(event.target.value)
              }
              required
            />
          </div>
        )}

        <div>
          <label>Email</label>
          <br />

          <input
            type="email"
            value={email}
            onChange={(event) =>
              setEmail(event.target.value)
            }
            required
          />
        </div>

        <div>
          <label>Password</label>
          <br />

          <input
            type="password"
            value={password}
            onChange={(event) =>
              setPassword(event.target.value)
            }
            required
          />
        </div>

        <br />

        <button type="submit">
          {isLogin ? "Login" : "Register"}
        </button>
      </form>

      <br />

      <button
        onClick={() => {
          setIsLogin(!isLogin);
          setMessage("");
        }}
      >
        {isLogin
          ? "Create an account"
          : "Already have an account? Login"}
      </button>

      <br />
      <br />

      <button onClick={getMyProfile}>
        Check Authentication
      </button>

      <p>{message}</p>
    </div>
  );
}

export default App;