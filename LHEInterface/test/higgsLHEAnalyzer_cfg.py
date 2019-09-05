import FWCore.ParameterSet.Config as cms

process = cms.Process("higgsLHE")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring('file:MCDBtoEDM_NONE.root')
    #fileNames = cms.untracked.vstring('file:MCDBtoEDM_WZmll0001_5.root')
    #fileNames = cms.untracked.vstring('file:MCDBtoEDM_ggHZ_NONE.root')
    #fileNames = cms.untracked.vstring(
    #    'file:myfile.root'
    #)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string("HWW2l2nuNNLOPS_LHEAnal.root"),
    #fileName = cms.string("MCDBtoEDM_WZmll0001_5.root_LHEAnal.root"),
    #fileName = cms.string("MCDBtoEDM_ggHZ_NONE_LHEAnal.root"),
    #closeFileFast = cms.untracked.bool(True)
    )

process.hAna = cms.EDAnalyzer('higgsLHEAnalyzer',
    src = cms.InputTag("source")
)


process.p = cms.Path(process.hAna)
