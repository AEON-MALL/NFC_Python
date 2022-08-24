import read,slack_post

while True:
    student_number = read.reader()
    slack_post.slack_post(student_number)