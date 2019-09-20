import os

VBFH = {'0PM':        ['anomalouscouplings/VBF_NNPDF31_13TeV/SM.input','WW2l2nu_withtaus.input'],
        '0M':         ['anomalouscouplings/VBF_NNPDF31_13TeV/a3.input','anomalouscouplings/WW2l2nu_withtaus_a3.input'],
        '0Mf05ph0':   ['anomalouscouplings/VBF_NNPDF31_13TeV/a3mix.input','anomalouscouplings/WW2l2nu_withtaus_a3mixforVBF.input'],
        '0PH':        ['anomalouscouplings/VBF_NNPDF31_13TeV/a2.input','anomalouscouplings/WW2l2nu_withtaus_a2.input'],
        '0PHf05ph0':  ['anomalouscouplings/VBF_NNPDF31_13TeV/a2mix.input','anomalouscouplings/WW2l2nu_withtaus_a2mixforVBF.input'],
        '0L1':        ['anomalouscouplings/VBF_NNPDF31_13TeV/L1.input','anomalouscouplings/WW2l2nu_withtaus_L1.input'],
        '0L1f05ph0':  ['anomalouscouplings/VBF_NNPDF31_13TeV/L1mix.input','anomalouscouplings/WW2l2nu_withtaus_L1mixforVBF.input'],
        '0L1Zgf05ph0':['anomalouscouplings/VBF_NNPDF31_13TeV/L1Zgmix.input','WW2l2nu_withtaus.input'],
    }
ZH = {'0PM':        ['anomalouscouplings/ZH_NNPDF31_13TeV/SM.input','WWany_filter2l.input'],
      '0M':         ['anomalouscouplings/ZH_NNPDF31_13TeV/a3.input','anomalouscouplings/WWany_filter2l_a3.input'],
      '0Mf05ph0':   ['anomalouscouplings/ZH_NNPDF31_13TeV/a3mix.input','anomalouscouplings/WWany_filter2l_a3mixforZH.input'],
      '0PH':        ['anomalouscouplings/ZH_NNPDF31_13TeV/a2.input','anomalouscouplings/WWany_filter2l_a2.input'],
      '0PHf05ph0':  ['anomalouscouplings/ZH_NNPDF31_13TeV/a2mix.input','anomalouscouplings/WWany_filter2l_a2mixforZH.input'],
      '0L1':        ['anomalouscouplings/ZH_NNPDF31_13TeV/L1.input','anomalouscouplings/WWany_filter2l_L1.input'],
      '0L1f05ph0':  ['anomalouscouplings/ZH_NNPDF31_13TeV/L1mix.input','anomalouscouplings/WWany_filter2l_L1mixforZH.input'],
      '0L1Zgf05ph0':['anomalouscouplings/ZH_NNPDF31_13TeV/L1Zgmix.input','WWany_filter2l.input'],
    }

WH = {'0PM':        ['anomalouscouplings/WH_NNPDF31_13TeV/SM.input','WWlnuany_filter2lOS.input'],
      '0M':         ['anomalouscouplings/WH_NNPDF31_13TeV/a3.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_a3.input'],
      '0Mf05ph0':   ['anomalouscouplings/WH_NNPDF31_13TeV/a3mix.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_a3mixforWH.input'],
      '0PH':        ['anomalouscouplings/WH_NNPDF31_13TeV/a2.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_a2.input'],
      '0PHf05ph0':  ['anomalouscouplings/WH_NNPDF31_13TeV/a2mix.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_a2mixforWH.input'],
      '0L1':        ['anomalouscouplings/WH_NNPDF31_13TeV/L1.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_L1.input'],
      '0L1f05ph0':  ['anomalouscouplings/WH_NNPDF31_13TeV/L1mix.input','anomalouscouplings/WWlnuany_withtaus_filter2lOS_L1mixforWH.input'],
    }

JJH ={'0PM':        ['anomalouscouplings/HJJ_NNPDF31_13TeV/SM.input','WW2l2nu_withtaus.input'],
      '0M':         ['anomalouscouplings/HJJ_NNPDF31_13TeV/a3.input','WW2l2nu_withtaus.input'],
      '0Mf05ph0':   ['anomalouscouplings/HJJ_NNPDF31_13TeV/a3mix.input','WW2l2nu_withtaus.input'],
    }

ttHWWany ={'0PM':        ['anomalouscouplings/ttH_NNPDF31_13TeV/SM.input','WWany_filter2lOS.input'],
           '0M':         ['anomalouscouplings/ttH_NNPDF31_13TeV/0M.input','WWany_filter2lOS.input'],
           '0Mf05ph0':   ['anomalouscouplings/ttH_NNPDF31_13TeV/0Mmix.input','WWany_filter2lOS.input'],
    }

ttHWWlnuany ={'0PM':        ['anomalouscouplings/ttH_NNPDF31_13TeV/SM.input','WWlnuany_filter2lOS.input'],
              '0M':         ['anomalouscouplings/ttH_NNPDF31_13TeV/0M.input','WWlnuany_filter2lOS.input'],
              '0Mf05ph0':   ['anomalouscouplings/ttH_NNPDF31_13TeV/0Mmix.input','WWlnuany_filter2lOS.input'],
    }
prodCardBase='cards/2017/13TeV/'
decayCardBase='cards/decay/'

for key in VBFH:
#for key in ttHWWlnuany:
#for key in ttHWWany:
#for key in JJH:
#for key in WH:
#for key in ZH:
  print "For coupling "+key

  #"""
  prodCard = prodCardBase+VBFH[key][0]
  decayCard = decayCardBase+VBFH[key][1]
  name = 'VBFHiggs'+key+'ToWWTo2L2Nu_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_VBFhWWTo2L2Nu_'+key+'.sh'
  #"""

  """
  prodCard = prodCardBase+ttHWWlnuany[key][0]
  decayCard = decayCardBase+ttHWWlnuany[key][1]
  name = 'ttHiggs'+key+'ToWWTolnuany_2lOS_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_tthWWTolnuany_2lOS_'+key+'.sh'
  """

  """
  prodCard = prodCardBase+ttHWWany[key][0]
  decayCard = decayCardBase+ttHWWany[key][1]
  name = 'ttHiggs'+key+'ToWWToany_2lOS_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_tthWWToany_2lOS_'+key+'.sh'
  """

  """
  prodCard = prodCardBase+JJH[key][0]
  decayCard = decayCardBase+JJH[key][1]
  name = 'JJHiggs'+key+'ToWWTo2L2Nu_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_JJhWWTo2L2Nu_'+key+'.sh'
  """

  """
  prodCard = prodCardBase+WH[key][0]
  decayCard = decayCardBase+WH[key][1]
  name = 'WHiggs'+key+'ToWWToLNu_2lOS_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_WhWWToLNu_2lOS_'+key+'.sh'
  """


  """
  prodCard = prodCardBase+ZH[key][0]
  decayCard = decayCardBase+ZH[key][1]
  name = 'ZHiggs'+key+'ToWW_2L_M-125_13TeV-JHU710'
  fileName='mkJHuJHU_ZhWW_2L_'+key+'.sh'
  """

  f=open(fileName,"w")
  f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/Generator/CMSSW_10_2_16_patch1/src/\n")
  #f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/\n")
  f.write("eval `scramv1 runtime -sh`\n")
  f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/Generator/CMSSW_10_2_16_patch1/src/genproductions/bin/JHUGen\n")
  #f.write("cd /afs/cern.ch/user/s/salee/WorkSpace/private/PowhegV2/CMSSW936ptch2/src/genproductions/bin/JHUGen\n")
  f.write("./install.py --card "+prodCard+" --decay-card "+decayCard+" --name "+name+"\n") # install_multi copied to install and PR
  #f.write("./install_multi.py --card "+prodCard+" --decay-card "+decayCard+" --name "+name+"\n")
  f.close()
  cmd = "chmod u+x "+fileName
  os.system(cmd)
  #subCmd='bsub -q 1nd '+fileName
  #os.system(subCmd)
