# CPSC 368 – Group 4

## Research Questions

1. How does average viewership and engagement of conservative and liberal YouTube channels change over time?
2. Is YouTube political engagement related to election outcomes?
3. Does YouTube comment sentiment reflect voter preferences or amplify extreme views?

## Channels

| Channel | Lean |
|---|---|
| Ben Shapiro / Daily Wire | Conservative |
| The Young Turks | Liberal |

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your API key

Create a `.env` file in the root directory:

```
API_KEY=your_api_key_here
ORACLE_USER=ora_yourCWL
ORACLE_PASSWORD=a12345678 (student number)

```

Get a key from [Google Cloud Console](https://console.cloud.google.com/). Daily quota is 10,000 units — this project uses ~6,000–8,000 units total so **run one channel at a time** and split across days if needed.

> Don't commit `.env` — it's in `.gitignore`.

---

## Running the Notebooks

All the scripts are in scripts/

We have a source_data directory meant to hold all our source data that's downloaded online and then cleaned_data is where final results can go. 

We can have a SQL folder for our sql scripts later

---

## Notes

- Checkpoints are saved in `checkpoints/` as JSON — don't delete these mid-collection
- Each channel gets its own `videos_<channel_name>.csv` in case of partial failures
- The `data/raw/` folder is gitignored — share data files via Google Drive