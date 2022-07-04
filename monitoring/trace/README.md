# steps

## install required library

    pip install -r requirements.txt
    opentelemetry-bootstrap -a install  # auto instrument lib

## run vanilla version

    FLASK_APP=vanilla flask run

## run auto instrument

    FLASK_APP=vanilla opentelemetry-instrument --traces_exporter console flask run

## run auto instrument with manual instrumentation

    FLASK_APP=manual opentelemetry-instrument --traces_exporter console flask run

## run full manual instrumentation

    FLASK_APP=full_manual flask run   ## this only has part of the function traced
    FLASK_APP=full_manual2 flask run  ## this also have access to "/" traced

## deploy service demo

    cd helm
    for s in {a..f}
      do
        helm install $s ./service-demo --set service_name=$s
    done