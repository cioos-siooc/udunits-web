# udunits-web

<https://units.server.hak4i.org/>

Simple [Dash](https://dash.plotly.com/) app to lookup units that are compatible with the [UDUNITS](https://www.unidata.ucar.edu/software/udunits/) library. Uses [cfunits](https://github.com/NCAS-CMS/cfunits) to interact with UDUNITS.

## Development

```sh
pip install -r requirements.txt
python app/app.py
```

## Deployment

Commits to the `app` directory are deployed to units.server.hak4i.org via Caprover.
