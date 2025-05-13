import kopf
import prometheus_client as prometheus

prometheus.start_http_server(9090)
TIMER = prometheus.Counter("run_second_total", "Total time object lived.")

@kopf.timer('kopfexamples',interval=15)
def timer_run_second_total(spec, logger, **_):
    print("TIMER.inc(15)")
    TIMER.inc(15)
