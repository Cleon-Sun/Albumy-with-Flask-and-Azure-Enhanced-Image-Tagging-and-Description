# Albumy with Flask and Azure: Enhanced Image Tagging and Description

## Overview

Albumy is a Flask-based web application for image sharing and management. This enhanced version integrates Azure's cognitive services to automatically generate tags and descriptions for uploaded images, making them easier to search and organize.

## Features

**Automatic Tagging**: Utilizes Azure's Computer Vision API to generate relevant tags for each uploaded image.
**Image Descriptions**: Automatically generates descriptive captions for images using Azure's AI capabilities.
**Easy Search**: Users can search for images based on tags and descriptions, improving accessibility and organization.



## How you can run this system:
In the terminal, please run:

```
cd albumy/blueprints
export endpoint='where_you_should_input_the_endpoint_for_ML'
export akey='here_you_should_input_the_key_for_ML'
flask run
```

then, you should be able to see the address of the system and open it in a browser

## How to get your own endpoint and key to use the ML features in the system

Please visit Microsoft Azure to subscripe to this service

## How to add additional libraries to requirements.txt for further extension

Please add more lines in the requirements.txt and run in the terminal

```
cd albumy
pip install -r requirements.txt
```
