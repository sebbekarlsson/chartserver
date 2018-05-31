# chartserver
> A server that serves charts over HTTP/HTTPS using Python & Flask.

## Usage
### Bar chart
> To retrieve a bar chart:

    GET /chart/bar/<xpoints>/<ypoints>

> Example:

    GET /chart/bar/a,b,c,g/10,0,30,10

> Will give you this image:

<img width='360px' src='images/barchart.png'/>

## Installing & Running
### Development mode
> First run the setup:

    python setup.py develop

> Then start the program:

    python __main__.py

> The server is now up and running at: `http://localhost:5000`

### Production mode
> coming soon
