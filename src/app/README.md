## Simulate a Jubilee line journey

test_app is a simple commandline script used to simulate a single run of the Jubilee line

### Usage (Python2 only at the moment )

```
python test_app --help
```

### Notes

For example, running

```
python test_app 1000
```

will run the Jubilee line simulation once (from Stratford to Stanmore) and initialise 1000 commuters.
Each commuter will have a randomly selected source station (Stanmore is not included) and a randomly
selected destination station. The simulation will monitor current time, the number of people currently
on the train and the number of people who are waiting in the resource queue.
At the end of the simulation, this data will be printed to stdout in the form [(time, number of commuters on train,
commuters waiting for space)]
