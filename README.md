# udunits-web

<https://units.server.hak4i.org/>

Simple [Dash](https://dash.plotly.com/) app to lookup units that are compatible with the [UDUNITS](https://www.unidata.ucar.edu/software/udunits/) library, which is useful for building [CF compliant](http://cfconventions.org/cf-conventions/cf-conventions.html) datasets. Uses [cfunits](https://github.com/NCAS-CMS/cfunits) to interact with UDUNITS.

## Development

```sh
conda create --name udunits_web python=3.10
conda activate udunits_web
pip install -f ./app/requirements.txt
conda install -c conda-forge udunits2>=2.2.25
python app/app.py
```

## Deployment

Commits to the `app` directory are deployed to units.server.hak4i.org via [Caprover](https://caprover.com/).
