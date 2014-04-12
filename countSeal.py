import praw
from sys import exit
import string
from pprint import pprint

r = praw.Reddit(user_agent='Testing some things')

submission = r.get_submission(submission_id='22t2vs')


def get_count(comment):
	count = 0
	if(hasattr(comment, 'body')):
		count = count + comment.body.count('seal')
	if(hasattr(comment, 'replies')):
		for reply in comment.replies:
			count = count + get_count(reply)
	return count



count = 0
for comment in submission.comments:
	count = count + get_count(comment)

print count
