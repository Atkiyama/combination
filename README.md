# Usage

1. Dockerfileの`CMD ["python", "./test2.py"]`のtest2.pyを実行したいファイル名にかえる
2. 以下を実行する

```sh
# Build the Docker image
docker build -t team_assignment .

# Run the Docker container
docker run team_assignment
```
