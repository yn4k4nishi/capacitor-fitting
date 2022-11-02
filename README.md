# capacitor-fitting
curve fitting for capacitor vs frequency

note : use only simsurfing data

| label | value | func |
| ---   | ---   | --- |
| [GJM1555C1H1R0BB01_InProduction.csv](img/GJM1555C1H1R0BB01_InProduction.png) | 1.0pF | `0.446 + 7.759e-03 * tan( freq/1e9 * 2.307e-03 + 1.55317 )` |
| [GJM1555C1H1R1BB01_InProduction.csv](img/GJM1555C1H1R1BB01_InProduction.png) | 1.1pF | `0.508 + 7.715e-03 * tan( freq/1e9 * 2.033e-03 + 1.55464 )` |
| [GJM1555C1H1R2BB01_InProduction.csv](img/GJM1555C1H1R2BB01_InProduction.png) | 1.2pF | `0.515 + 9.215e-03 * tan( freq/1e9 * 2.215e-03 + 1.55384 )` |
| [GJM1555C1H1R3BB01_InProduction.csv](img/GJM1555C1H1R3BB01_InProduction.png) | 1.3pF | `0.516 + 1.648e-02 * tan( freq/1e9 * 3.652e-03 + 1.54382 )` |
| [GJM1555C1H1R4BB01_InProduction.csv](img/GJM1555C1H1R4BB01_InProduction.png) | 1.4pF | `0.530 + 2.301e-02 * tan( freq/1e9 * 4.747e-03 + 1.53639 )` |
| [GJM1555C1H1R5BB01_InProduction.csv](img/GJM1555C1H1R5BB01_InProduction.png) | 1.5pF | `0.500 + 5.973e-02 * tan( freq/1e9 * 1.150e-02 + 1.49012 )` |
| [GJM1555C1H1R6BB01_InProduction.csv](img/GJM1555C1H1R6BB01_InProduction.png) | 1.6pF | `0.527 + 6.705e-02 * tan( freq/1e9 * 1.248e-02 + 1.48605 )` |
| [GJM1555C1H1R7BB01_InProduction.csv](img/GJM1555C1H1R7BB01_InProduction.png) | 1.7pF | `0.737 + 6.072e-02 * tan( freq/1e9 * 1.229e-02 + 1.48867 )` |
| [GJM1555C1H1R8BB01_InProduction.csv](img/GJM1555C1H1R8BB01_InProduction.png) | 1.8pF | `0.756 + 6.549e-02 * tan( freq/1e9 * 1.264e-02 + 1.48844 )` |
| [GJM1555C1H1R9BB01_InProduction.csv](img/GJM1555C1H1R9BB01_InProduction.png) | 1.9pF | `0.774 + 6.380e-02 * tan( freq/1e9 * 1.179e-02 + 1.49580 )` |
| [GJM1555C1H2R0BB01_InProduction.csv](img/GJM1555C1H2R0BB01_InProduction.png) | 2.0pF | `0.728 + 6.880e-02 * tan( freq/1e9 * 1.165e-02 + 1.49819 )` |
| [GJM1555C1H2R1BB01_InProduction.csv](img/GJM1555C1H2R1BB01_InProduction.png) | 2.1pF | `0.754 + 8.282e-02 * tan( freq/1e9 * 1.360e-02 + 1.48801 )` |
| [GJM1555C1H2R2BB01_InProduction.csv](img/GJM1555C1H2R2BB01_InProduction.png) | 2.2pF | `0.785 + 7.863e-02 * tan( freq/1e9 * 1.256e-02 + 1.49601 )` |
| [GJM1555C1H2R3BB01_InProduction.csv](img/GJM1555C1H2R3BB01_InProduction.png) | 2.3pF | `1.099 + 6.886e-02 * tan( freq/1e9 * 1.348e-02 + 1.49406 )` |
| [GJM1555C1H2R4BB01_InProduction.csv](img/GJM1555C1H2R4BB01_InProduction.png) | 2.4pF | `1.133 + 7.643e-02 * tan( freq/1e9 * 1.443e-02 + 1.49005 )` |
| [GJM1555C1H2R5BB01_InProduction.csv](img/GJM1555C1H2R5BB01_InProduction.png) | 2.5pF | `1.160 + 7.962e-02 * tan( freq/1e9 * 1.450e-02 + 1.49096 )` |
| [GJM1555C1HR10BB01_InProduction.csv](img/GJM1555C1HR10BB01_InProduction.png) | 0.1pF | `0.092 + 3.410e-05 * tan( freq/1e9 * 3.710e-04 + 1.56597 )` |
| [GJM1555C1HR20BB01_InProduction.csv](img/GJM1555C1HR20BB01_InProduction.png) | 0.2pF | `0.170 + 2.088e-04 * tan( freq/1e9 * 6.529e-04 + 1.56287 )` |
| [GJM1555C1HR30BB01_InProduction.csv](img/GJM1555C1HR30BB01_InProduction.png) | 0.3pF | `0.241 + 4.287e-04 * tan( freq/1e9 * 7.254e-04 + 1.56251 )` |
| [GJM1555C1HR40BB01_InProduction.csv](img/GJM1555C1HR40BB01_InProduction.png) | 0.4pF | `0.292 + 3.791e-04 * tan( freq/1e9 * 3.748e-04 + 1.56677 )` |
| [GJM1555C1HR50BB01_InProduction.csv](img/GJM1555C1HR50BB01_InProduction.png) | 0.5pF | `0.355 + 7.252e-04 * tan( freq/1e9 * 5.633e-04 + 1.56500 )` |
| [GJM1555C1HR60BB01_InProduction.csv](img/GJM1555C1HR60BB01_InProduction.png) | 0.6pF | `0.397 + 6.110e-04 * tan( freq/1e9 * 3.578e-04 + 1.56728 )` |
| [GJM1555C1HR70BB01_InProduction.csv](img/GJM1555C1HR70BB01_InProduction.png) | 0.7pF | `0.408 + 2.152e-03 * tan( freq/1e9 * 9.738e-04 + 1.56202 )` |
| [GJM1555C1HR80BB01_InProduction.csv](img/GJM1555C1HR80BB01_InProduction.png) | 0.8pF | `0.435 + 2.388e-03 * tan( freq/1e9 * 9.192e-04 + 1.56289 )` |
| [GJM1555C1HR90BB01_InProduction.csv](img/GJM1555C1HR90BB01_InProduction.png) | 0.9pF | `0.462 + 4.369e-03 * tan( freq/1e9 * 1.486e-03 + 1.55859 )` |
| [GRM1554C1HR40BA01_NotRecommended.csv](img/GRM1554C1HR40BA01_NotRecommended.png) | 0.4pF | `0.277 + 4.051e-04 * tan( freq/1e9 * 3.735e-04 + 1.56699 )` |
| [GRM1554C1HR60BA01_NotRecommended.csv](img/GRM1554C1HR60BA01_NotRecommended.png) | 0.6pF | `0.349 + 1.039e-03 * tan( freq/1e9 * 5.526e-04 + 1.56586 )` |
| [GRM1554C1HR80BA01_NotRecommended.csv](img/GRM1554C1HR80BA01_NotRecommended.png) | 0.8pF | `0.390 + 3.855e-03 * tan( freq/1e9 * 1.466e-03 + 1.55916 )` |
