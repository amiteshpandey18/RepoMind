import { useState } from "react";


function Register({ onShowLogin }) {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);


    const handleRegister = async (event) => {

        event.preventDefault();

        if (!username || !email || !password) {
            setError("Please fill in all fields.");
            return;
        }

        setError("");
        setMessage("");
        setLoading(true);


        try {

            const response = await fetch(
                "http://127.0.0.1:8000/auth/register",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        username: username,
                        email: email,
                        password: password
                    })
                }
            );


            const data = await response.json();


            if (!response.ok) {
                throw new Error(
                    data.detail || "Registration failed"
                );
            }


            setMessage(
                "Registration successful. You can now login."
            );

            setUsername("");
            setEmail("");
            setPassword("");


        } catch (error) {

            setError(error.message);

        } finally {

            setLoading(false);

        }
    };


    return (
        <div className="auth-page">

            <div className="auth-card">

                <div className="auth-header">

                    <h1>RepoMind</h1>

                    <p>
                        AI assistant for your GitHub repositories
                    </p>

                </div>


                <h2>Create account</h2>

                <p className="auth-subtitle">
                    Create your RepoMind account
                </p>


                <form onSubmit={handleRegister}>

                    <label>Username</label>

                    <input
                        type="text"
                        value={username}
                        onChange={(event) =>
                            setUsername(event.target.value)
                        }
                        placeholder="Enter your username"
                    />


                    <label>Email</label>

                    <input
                        type="email"
                        value={email}
                        onChange={(event) =>
                            setEmail(event.target.value)
                        }
                        placeholder="Enter your email"
                    />


                    <label>Password</label>

                    <input
                        type="password"
                        value={password}
                        onChange={(event) =>
                            setPassword(event.target.value)
                        }
                        placeholder="Create a password"
                    />


                    {error && (
                        <p className="auth-error">
                            {error}
                        </p>
                    )}


                    {message && (
                        <p className="auth-success">
                            {message}
                        </p>
                    )}


                    <button
                        type="submit"
                        disabled={loading}
                    >
                        {loading
                            ? "Creating account..."
                            : "Register"}
                    </button>

                </form>


                <p className="auth-switch">

                    Already have an account?

                    <button
                        type="button"
                        onClick={onShowLogin}
                    >
                        Login
                    </button>

                </p>

            </div>

        </div>
    );
}


export default Register;