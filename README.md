# chartserver
> A server that serves charts over HTTP/HTTPS.

## Usage
### Bar chart
> To retrieve a bar chart:

    GET /chart/bar/<xpoints>/<ypoints>

> Example:

    GET /chart/bar/a,b,c,g/10,0,30,10

> Will give you this image:

<img width='360px' src='images/barchart.png'/>
