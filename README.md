# capacitor-fitting
curve fitting for capacitor vs frequency

note : use only simsurfing data

| label | value | func |
| ---   | ---   | --- |
| [GJM1555C1HR50BB01_InProduction.csv](img/GJM1555C1HR50BB01_InProduction.png) | 0.5pF | `0.288 + 2.276e-03 * tan( freq/1e9 * 1.095e-03 + 1.55815 )` |
