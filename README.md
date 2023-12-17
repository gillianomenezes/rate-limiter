# Django Rate Limiter Example

Implement a simple Django rate limiter without third-party libraries. This project restricts requests per minute by client IP, preventing abuse and ensuring fair resource usage. Dockerized for easy deployment.

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/gillianomenezes/rate-limiter.git
    cd django-rate-limiter
    ```

2. **Build the Docker image:**

    ```bash
    docker build -t django-rate-limiter .
    ```

3. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 django-rate-limiter
    ```

4. **Access the example view:**

    Open your web browser and go to [http://localhost:8000/rate/](http://localhost:8000/rate/)

## Project Structure

- `rate_limiter/`: Django project folder.
- `rate/`: Django app folder containing the rate limiter implementation.
- `Dockerfile`: Configuration for building the Docker image.
- `docker-compose.yml`: Docker Compose configuration for easier deployment.
- `requirements.txt`: Project dependencies.

## Contributing

Contributions are welcome! Please follow our [Contribution Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, feel free to reach out to me:

- [Email](mailto:gillianomenezes@gmail.com)
- [Twitter](https://twitter.com/gillianomenezes)
- [LinkedIn](https://www.linkedin.com/in/gillianomenezes/)

Enjoy coding!

