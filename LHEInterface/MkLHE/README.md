# Making LHE



## Purpose
```
Making a LHE file.
```

## Making a LHE file from a McM configuration
 * Download test McM script using **getTestScriptFrMcM.sh**
 * In the McMScript, first comment out "if grep -q "gridpacks" ...." and all the below lines to get the configuration file.
 * After you run the McMScript, you will get the configuration file. Its location should look like:
 /afs/cern.ch/work/j/jihunk/private/powhegtutorial_mkLHE/CMSSW_10_2_6/src/Configuration/GenProduction/python/HIG-RunIIFall18wmLHEGS-00933-fragment.py
 * Open the configuration file.
 * At McM, usually the arge is like "args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/powheg/V2/HWminusJ_HanythingJ_NNPDF31_13TeV_M125/HWJ_slc6_amd64_gcc630_CMSSW_9_3_0_HWminusJ_HanythingJ_NNPDF31_13TeV_M125_Vinclusive.tgz')," for the official location for the grid generation.
 * But for the local generation, you can put it like "/afs/cern.ch/user/s/salee/WorkSpace/public/GridPacks/HWJ/HWJ_slc6_amd64_gcc630_CMSSW_9_3_0_HWminusJ_HWWany_NNPDF31_13TeV_M125_Vinc_JHU724.tgz"
 * Now go back to the McMScript, reduce the comment and run again. (Note: handle the number of generation using -n <number>) The end of the local generation.
 * If you want to use condor, go to the McMScript, write the below in the beginning of the script,
 ```
 export X509_USER_PROXY=$1
 voms-proxy-info -all
 voms-proxy-info -all -file $1
 ```
 * ./condor\_submit.sh
 * In both way, you will get a root file.

## Checking a created LHE file
 * Modify genTable_cfg.py 
 ```
 fileNames = cms.untracked.vstring('file:HIG-RunIIFall18wmLHEGS-00581.root'),
 src = cms.InputTag("prunedGenParticles"), for miniAod
 src = cms.InputTag("genParticles"), for reco, yes this one
 ```
 cmsRun genTable\_cfg.py >& your.list



