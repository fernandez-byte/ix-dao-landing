"""
IX DAO Twitter Tool
Usage:
  python twitter.py post "Your tweet text here"
  python twitter.py thread "Line 1" "Line 2" "Line 3"
  python twitter.py report
  python twitter.py profile
"""

import sys
import os
import json
import tweepy
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    bearer_token=os.getenv("X_BEARER_TOKEN"),
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
    wait_on_rate_limit=True
)


def post_tweet(text):
    try:
        response = client.create_tweet(text=text)
        tweet_id = response.data["id"]
        print(f"[OK] Tweet posted!")
        print(f"   ID: {tweet_id}")
        print(f"   URL: https://x.com/i/web/status/{tweet_id}")
        return tweet_id
    except tweepy.TweepyException as e:
        print(f"[ERROR] {e}")
        return None


def post_thread(tweets):
    if not tweets:
        print("[ERROR] No tweets provided.")
        return

    print(f"[THREAD] Posting thread ({len(tweets)} tweets)...")
    previous_id = None
    for i, text in enumerate(tweets, 1):
        try:
            if previous_id:
                response = client.create_tweet(text=text, in_reply_to_tweet_id=previous_id)
            else:
                response = client.create_tweet(text=text)
            previous_id = response.data["id"]
            print(f"   [{i}/{len(tweets)}] [OK] {text[:50]}...")
        except tweepy.TweepyException as e:
            print(f"   [{i}] [ERROR] Error: {e}")
            break

    print(f"\n[OK] Thread posted! First tweet: https://x.com/i/web/status/{previous_id}")


def get_profile():
    try:
        me = client.get_me(user_fields=["public_metrics", "description", "created_at"], user_auth=True)
        user = me.data
        metrics = user.public_metrics
        print("\n-- IX DAO Twitter Profile ------------------")
        print(f"  Handle      : @{user.username}")
        print(f"  Name        : {user.name}")
        print(f"  Followers   : {metrics['followers_count']:,}")
        print(f"  Following   : {metrics['following_count']:,}")
        print(f"  Tweets      : {metrics['tweet_count']:,}")
        print(f"  Bio         : {user.description}")
        print("---------------------------------------------\n")
    except tweepy.TweepyException as e:
        print(f"[ERROR] Error: {e}")


def generate_report():
    try:
        me = client.get_me(user_fields=["public_metrics", "description"], user_auth=True)
        user = me.data
        metrics = user.public_metrics

        tweets = client.get_users_tweets(
            id=user.id,
            max_results=10,
            tweet_fields=["public_metrics", "created_at"],
            exclude=["retweets", "replies"]
        )

        total_likes = 0
        total_retweets = 0
        total_replies = 0
        total_impressions = 0
        top_tweet = None
        top_score = 0

        now = datetime.now(timezone.utc)
        print("\n══════════════════════════════════════════════")
        print("  IX DAO — Twitter Insight Report")
        print(f"  Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}")
        print("==============================================")
        print(f"\n  Account   : @{user.username}")
        print(f"  Followers : {metrics['followers_count']:,}")
        print(f"  Following : {metrics['following_count']:,}")
        print(f"  Total Tweets: {metrics['tweet_count']:,}")

        if tweets.data:
            print(f"\n-- Last {len(tweets.data)} Tweets ----------------------------")
            for t in tweets.data:
                m = t.public_metrics
                likes = m.get("like_count", 0)
                rts = m.get("retweet_count", 0)
                replies = m.get("reply_count", 0)
                impressions = m.get("impression_count", 0)
                score = likes + rts * 2 + replies
                total_likes += likes
                total_retweets += rts
                total_replies += replies
                total_impressions += impressions
                if score > top_score:
                    top_score = score
                    top_tweet = t
                created = t.created_at.strftime("%Y-%m-%d") if t.created_at else "N/A"
                print(f"\n  [{created}] {t.text[:70]}...")
                print(f"  Likes: {likes}  RT: {rts}  Replies: {replies}  Impressions: {impressions}")

            print("\n-- Summary -----------------------------------")
            print(f"  Total Likes       : {total_likes}")
            print(f"  Total Retweets    : {total_retweets}")
            print(f"  Total Replies     : {total_replies}")
            print(f"  Total Impressions : {total_impressions}")
            if top_tweet:
                print(f"\n  Top Tweet:")
                print(f"  {top_tweet.text[:80]}...")
                print(f"  https://x.com/i/web/status/{top_tweet.id}")
        else:
            print("\n  No recent tweets found.")

        print("\n══════════════════════════════════════════════\n")

    except tweepy.TweepyException as e:
        print(f"[ERROR] Error: {e}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1].lower()

    if command == "post":
        if len(sys.argv) < 3:
            print("Usage: python twitter.py post \"Your tweet here\"")
            return
        post_tweet(sys.argv[2])

    elif command == "thread":
        if len(sys.argv) < 4:
            print("Usage: python twitter.py thread \"Tweet 1\" \"Tweet 2\" ...")
            return
        post_thread(sys.argv[2:])

    elif command == "report":
        generate_report()

    elif command == "profile":
        get_profile()

    else:
        print(f"Unknown command: {command}")
        print(__doc__)


if __name__ == "__main__":
    main()
