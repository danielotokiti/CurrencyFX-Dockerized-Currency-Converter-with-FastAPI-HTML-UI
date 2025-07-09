Day 2 - CI/CD Pipeline + Security Scans + Docker Hub Delivery

**Tasks Completed:
- Created a GitHub Actions pipeline in .github/workflows/main.yml to automate:
    Cloning the latest code from GitHub on every push to the master branch.
    Building the Docker image using the tested Dockerfile.
    Running a Trivy vulnerability scan, caching both the CVE database and image layer metadata to make future scans faster while still catching new CVEs.
    Logging into Docker Hub using secure GitHub repository secrets, and pushing the image to my repo.
- Used VS Code to stage, commit, and push code changes to GitHub, automatically triggering the pipeline on the master branch.
- Verified in the GitHub Actions console that all steps completed successfully, including security scanning and pushing to Docker Hub.
- Confirmed the new image appeared in the Docker Hub repository (danielotokiti/currencyserv), demonstrating successful automated delivery.
- Pulled and ran the container from Docker Hub to test if push action worked fine.



Screenshots:
- VS Code terminal & source control showing git add, git commit, and git push to the master branch.
- .github/workflows directory and main.yml pipeline file in editor.
- GitHub Actions run: passing all jobs (checkout, build, Trivy scan, push to Docker Hub).
- Trivy scan logs showing cache hits + no critical vulnerabilities.
- Docker Hub repository with the currencyserv:latest image tag and build timestamp.
- Local pull & run of the Docker image with the app verified in the browser.
