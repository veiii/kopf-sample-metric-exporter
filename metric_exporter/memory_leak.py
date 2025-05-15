from memory_profiler import profile

import kopf

output_file = open('tests/memory_profile.log', 'w')

@kopf.timer(
    'kopfexamples',
    interval=5,
    initial_delay=1,
    id="my-problematic-reload2",
)
@profile(stream=output_file)
def on_my_problematic_reload2(memo: kopf.Memo, patch, **kwargs):
   patch.status["ready"] = True

@profile(stream=output_file)
@kopf.timer(
    'kopfexamples',
    interval=2,
    initial_delay=1,
    id="my-problematic-reload",
)
def on_my_problematic_reload(memo: kopf.Memo, patch, **kwargs):
   patch.status["ready"] = True

@profile(stream=output_file)
@kopf.timer(
    'kopfexamples',
    interval=2,
    initial_delay=1,
    id="my-problematic-reload3",
)
def on_my_problematic_reload3(memo: kopf.Memo, patch, **kwargs):
   patch.status["ready"] = True