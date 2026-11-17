/* Authored-but-not-executed reference: the real SAS PROC POWER
   workflow this sample-size calculator would use in production. No
   SAS installation is available in this environment, so
   src/sample_size_calculator.py implements the identical 5 study-
   design templates via genuine Monte Carlo power simulation in
   Python as the executed mirror, and all measured results in this
   repo come from that mirror. */

proc power;
    twosamplemeans test=diff
        meandiff = 0.5
        stddev = 1
        power = 0.8
        ntotal = .;
run;

proc power;
    pairedmeans test=diff
        meandiff = 0.4
        stddev = 1
        power = 0.8
        npairs = .;
run;

proc power;
    twosamplefreq test=pchi
        groupproportions = (0.3 0.5)
        power = 0.8
        ntotal = .;
run;
