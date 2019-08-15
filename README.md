# study_english-word_app

This application is English word learnig app for me.

## Summary

Ten English words will be randomly asked one question at a time.   
Can customize the question by part of speech.   

## Motivation to make

Then I want to improve English ability.   
Because, when I went to Thailand a month ago, I can not speak English very well.   
And I often watch youtube about Python, Golang, and so on.
I think I am more happy if I would speak and listen to English.
So I desided to stady English.
This is my First step learn English.

## Architecture

## Functions

|orverview|method|uri|
|---|---|---|
|show words|GET|words/|
|show word|GET|words/`<id>`|
|create word|POST|words/|
|delete word|DELETE|words/`<id>`|

## Database
### Tables
* words
* part_of_speech( will be normalized in the future)
* meaning( will be normalized in the future)
* test_result

### Columns(word)
|name|type|default|nullable|
|---|---|---|---|
|id|int|auto|no|
|name|char(50)||no|
|mean1|char(100)||no|
|mean2|char(100)|blank|yes|
|mean3|char(100)|blank|yes|
|logical_delete_flag|bool|False|no|
