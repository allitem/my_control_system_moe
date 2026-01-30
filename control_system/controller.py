def run_pipeline_version(repo, version="default"):
    print(f"Running {repo} with Python {version}")
    return {"repo": repo, "version": version, "status": "success"}
