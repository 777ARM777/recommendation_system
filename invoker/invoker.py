from flask import Flask, jsonify
from cachetools import TTLCache
import redis
import requests
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

local_cache = TTLCache(maxsize=3, ttl=10)
redis_cache = redis.Redis(host='redis', port=6379, db=0)


def runcascade(viewer_id):
    models = ['model1', 'model2', 'model3', 'model4', 'model5']
    results = []
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(requests.post, 'http://generator:5000/generate', json={'model_name': model, 'viewer_id': viewer_id}) for model in models]
        for future in futures:
            result = future.result().json()
            results.append(result)

    return results

@app.route('/recommend/<viewer_id>', methods=['GET'])
def recommend(viewer_id):
    if viewer_id in local_cache:
        return jsonify(local_cache[viewer_id])

    cached_data = redis_cache.get(viewer_id)
    if cached_data:
        cached_data = eval(cached_data)
        local_cache[viewer_id] = cached_data
        return jsonify(cached_data)

    recommendations = runcascade(viewer_id)
    local_cache[viewer_id] = recommendations
    redis_cache.set(viewer_id, str(recommendations))

    return jsonify(recommendations)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
