# Higher or Lower: Instagram Followers Game

## Overview

Higher or Lower: Instagram Followers Edition is a fun and interactive game where players guess whether a given celebrity or influencer has more or fewer Instagram followers than another. The goal is to get as many correct guesses as possible in a row!

## Short Description

Test your knowledge of Instagram's most-followed celebrities in this addictive Higher or Lower game! Players are presented with two famous personalities and must guess if the second has more or fewer followers than the first. With a dynamic database of influencers and celebrities, the game provides a fun challenge for social media enthusiasts. Score as many correct guesses as possible before making a mistake!

## How to Play

1. The game presents two famous personalities with their names and countries.
2. The player must guess whether the second person has **higher** or **lower** followers compared to the first.
3. If the guess is correct, the game continues with a new comparison.
4. If the guess is wrong, the game ends, and the player receives their final score.

## Features

- Randomized selection of Instagram personalities.
- Simple and engaging user interface.
- Playable in single-player mode.

## Data Structure

The game uses a list of dictionaries to store Instagram follower data, including:

```python
instagram_followers_data = [
    {"name": "Cristiano Ronaldo", "followers": 625000000, "country": "Portugal"},
    {"name": "Lionel Messi", "followers": 500000000, "country": "Argentina"},
    {"name": "Selena Gomez", "followers": 430000000, "country": "USA"},
    # More entries...
]
```

## Installation & Running the Game

### Prerequisites

- Python 3.x

### Steps

1. Clone or download this repository.
2. Install dependencies if required (`pip install -r requirements.txt`).
3. Run the game script:
   ```bash
   python higherlower.py
   ```

## Future Enhancements

- **Leaderboard System:** Track top scores for competitive gameplay.
- **API Integration:** Fetch live follower counts dynamically.
- **Multiplayer Mode:** Challenge friends in real-time.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

This project is open-source and free to use. Contributions are welcome!

## Contributing

If you'd like to contribute, feel free to fork the repository and submit a pull request!

---

Have fun playing the Higher or Lower: Instagram Followers Edition! 🚀


