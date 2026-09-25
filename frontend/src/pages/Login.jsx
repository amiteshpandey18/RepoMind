import { useState } from "react";


function Login({ onLogin, onShowRegister }) {

    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);


    const handleLogin = async (event) => {

        event.preventDefault();

        if (!email || !password) {
            setError("Please enter email and password.");
            return;
        }

        setError("");
        setLoading(true);


        try {

            const response = await fetch(
                "http://127.0.0.1:8000/auth/login",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({
                        email: email,
                        password: password
                    })
                }
            );


            const data = await response.json();


            if (!response.ok) {
                throw new Error(
                    data.detail || "Login failed"
                );
            }


            localStorage.setItem(
                "access_token",
                data.access_token
            );

            onLogin();

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


                <h2>Welcome back</h2>

                <p className="auth-subtitle">
                    Login to continue to RepoMind
                </p>


                <form onSubmit={handleLogin}>

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
                        placeholder="Enter your password"
                    />


                    {error && (
                        <p className="auth-error">
                            {error}
                        </p>
                    )}


                    <button
                        type="submit"
                        disabled={loading}
                    >
                        {loading ? "Logging in..." : "Login"}
                    </button>

                </form>


                <p className="auth-switch">

                    Don't have an account?

                    <button
                        type="button"
                        onClick={onShowRegister}
                    >
                        Register
                    </button>

                </p>

            </div>

        </div>
    );
}


export default Login;