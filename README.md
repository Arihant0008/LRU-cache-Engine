# LRU Cache Engine

A custom-engineered, in-memory caching system implementing an $O(1)$ Least Recently Used (LRU) eviction policy, built with Python and served via a FastAPI REST interface.

## Overview

This project combines a doubly linked list and a hash map to provide constant-time cache reads, writes, and recency updates. The cache is exposed through a small FastAPI application, making it easy to test and integrate with HTTP clients.

## Features

- $O(1)$ `get` and `put` operations
- Deterministic LRU eviction when capacity is exceeded
- FastAPI REST endpoints for interacting with the cache
- Lightweight, dependency-friendly Python implementation

## How It Works

The cache keeps the most recently used item near the front of a linked list and the least recently used item near the back. A dictionary provides direct access to nodes by key, while the linked list maintains usage order. When the cache reaches capacity, the least recently used item is removed in constant time.

## Project Structure

- `phase1.py`: Core LRU cache implementation
- `server.py`: FastAPI application exposing cache endpoints

## API Endpoints

### `GET /get/{key}`

Returns the cached value for the requested key.

Response example:

```json
{
  "key": 1,
  "value": "A"
}
```

If the key is not present, the service returns `404 Not Found`.

### `POST /put`

Stores or updates a cache entry.

Request body:

```json
{
  "key": 1,
  "value": "A"
}
```

Response example:

```json
{
  "message": "Successfully cached 1"
}
```

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`

### Install Dependencies

```bash
pip install fastapi uvicorn
```

### Run the API

```bash
uvicorn server:app --reload
```

If `uvicorn` is not available as a command, run:

```bash
python -m uvicorn server:app --reload
```

### Try It

Open the interactive docs at:

```text
http://127.0.0.1:8000/docs
```

## Example Usage

1. Send a `POST /put` request to add a value.
2. Send a `GET /get/{key}` request to retrieve it.
3. Add more than the configured capacity to observe LRU eviction.

## Notes

- The current cache capacity is set in `server.py`.
- `phase1.py` includes a small inline demonstration at the bottom of the file.
