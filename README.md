# capacitor-fitting
curve fitting for capacitor vs frequency

note : use only simsurfing data

| label | value | func |
| ---   | ---   | --- |
| [GJM1555C1H1R0BB01_InProduction.csv](img/GJM1555C1H1R0BB01_InProduction.png) | 1.0pF | `0.381 + 4.215e-02 * tan( freq/1e9 * 1.148e-02 + 1.48250 )` |
| [GJM1555C1H2R0BB01_InProduction.csv](img/GJM1555C1H2R0BB01_InProduction.png) | 2.0pF | `0.764 + 7.817e-02 * tan( freq/1e9 * 1.326e-02 + 1.48818 )` |
| [GJM1555C1HR10BB01_InProduction.csv](img/GJM1555C1HR10BB01_InProduction.png) | 0.1pF | `0.088 + 4.483e-05 * tan( freq/1e9 * 2.608e-04 + 1.56661 )` |
| [GJM1555C1HR20BB01_InProduction.csv](img/GJM1555C1HR20BB01_InProduction.png) | 0.2pF | `0.156 + 2.552e-04 * tan( freq/1e9 * 4.482e-04 + 1.56428 )` |
| [GJM1555C1HR30BB01_InProduction.csv](img/GJM1555C1HR30BB01_InProduction.png) | 0.3pF | `0.214 + 4.519e-04 * tan( freq/1e9 * 4.465e-04 + 1.56483 )` |
| [GJM1555C1HR40BB01_InProduction.csv](img/GJM1555C1HR40BB01_InProduction.png) | 0.4pF | `0.242 + 1.246e-03 * tan( freq/1e9 * 7.448e-04 + 1.56167 )` |
| [GJM1555C1HR50BB01_InProduction.csv](img/GJM1555C1HR50BB01_InProduction.png) | 0.5pF | `0.288 + 2.276e-03 * tan( freq/1e9 * 1.095e-03 + 1.55815 )` |
| [GJM1555C1HR60BB01_InProduction.csv](img/GJM1555C1HR60BB01_InProduction.png) | 0.6pF | `0.300 + 2.304e-03 * tan( freq/1e9 * 8.592e-04 + 1.56151 )` |
| [GJM1555C1HR70BB01_InProduction.csv](img/GJM1555C1HR70BB01_InProduction.png) | 0.7pF | `0.268 + 3.050e-02 * tan( freq/1e9 * 9.632e-03 + 1.47910 )` |
| [GJM1555C1HR80BB01_InProduction.csv](img/GJM1555C1HR80BB01_InProduction.png) | 0.8pF | `0.305 + 3.436e-02 * tan( freq/1e9 * 1.011e-02 + 1.48060 )` |
| [GJM1555C1HR90BB01_InProduction.csv](img/GJM1555C1HR90BB01_InProduction.png) | 0.9pF | `0.354 + 3.770e-02 * tan( freq/1e9 * 1.065e-02 + 1.48146 )` |
