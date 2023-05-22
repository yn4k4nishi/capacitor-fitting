# capacitor-fitting
curve fitting for capacitor vs frequency

note : use only simsurfing data

| label | value | func |
| ---   | ---   | --- |
| [GJM1555C1HR40BB01_InProduction.csv](img/GJM1555C1HR40BB01_InProduction.png) | 0.4pF | `0.242 + 1.246e-03 * tan( freq/1e9 * 7.448e-04 + 1.56167 )` |
| [GJM1555C1HR50BB01_InProduction.csv](img/GJM1555C1HR50BB01_InProduction.png) | 0.5pF | `0.288 + 2.276e-03 * tan( freq/1e9 * 1.095e-03 + 1.55815 )` |
| [GJM1555C1HR60BB01_InProduction.csv](img/GJM1555C1HR60BB01_InProduction.png) | 0.6pF | `0.300 + 2.304e-03 * tan( freq/1e9 * 8.592e-04 + 1.56151 )` |
| [GJM1555C1HR70BB01_InProduction.csv](img/GJM1555C1HR70BB01_InProduction.png) | 0.7pF | `0.268 + 3.050e-02 * tan( freq/1e9 * 9.632e-03 + 1.47910 )` |
