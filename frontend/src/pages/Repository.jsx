import { useState } from "react";


function Repository({ onRepositoryConnected }) {

    const [repositoryUrl, setRepositoryUrl] = useState("");
    const [error, setError] = useState("");
    const [loading, setLoading] = useState(false);


    const connectRepository = async (event) => {

        event.preventDefault();

        if (!repositoryUrl.trim()) {
            setError("Please enter a GitHub repository URL.");
            return;
        }

        setError("");
        setLoading(true);


        try {

            const url = new URL(repositoryUrl);

            if (url.hostname !== "github.com") {
                throw new Error(
                    "Please enter a valid GitHub repository URL."
                );
            }


            const parts = url.pathname
                .split("/")
                .filter(Boolean);


            if (parts.length < 2) {
                throw new Error(
                    "Please enter a valid repository URL."
                );
            }


            const owner = parts[0];
            const repo = parts[1].replace(".git", "");


            const response = await fetch(
                `http://127.0.0.1:8000/github/${owner}/${repo}`
            );


            const data = await response.json();


            if (!response.ok || data.message === "Repository not found") {
                throw new Error(
                    "Repository not found or could not be accessed."
                );
            }


            localStorage.setItem(
                "repository_owner",
                owner
            );

            localStorage.setItem(
                "repository_name",
                repo
            );


            onRepositoryConnected({
                owner: owner,
                repo: repo,
                data: data
            });


        } catch (error) {

            console.error(error);

            setError(
                error.message ||
                "Unable to connect repository."
            );

        } finally {

            setLoading(false);

        }
    };


    return (
        <div className="auth-page">

            <div className="auth-card repository-card">

                <div className="auth-header">

                    <div className="repository-icon">
                        ⌘
                    </div>

                    <h1>RepoMind</h1>

                    <p>
                        AI assistant for your GitHub repositories
                    </p>

                </div>


                <h2>Connect a repository</h2>

                <p className="auth-subtitle">
                    Enter the GitHub repository you want to explore.
                </p>


                <form onSubmit={connectRepository}>

                    <label>
                        GitHub Repository URL
                    </label>

                    <input
                        type="url"
                        value={repositoryUrl}
                        onChange={(event) =>
                            setRepositoryUrl(event.target.value)
                        }
                        placeholder="https://github.com/user/repository"
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
                        {loading
                            ? "Connecting..."
                            : "Connect Repository"}
                    </button>

                </form>


                <p className="repository-example">
                    Example:
                    <br />
                    https://github.com/amiteshpandey18/RepoMind
                </p>

            </div>

        </div>
    );
}


export default Repository;