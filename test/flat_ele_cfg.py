import FWCore.ParameterSet.Config as cms

process = cms.Process("HoE")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('PhysicsTools.HepMCCandAlgos.genParticles_cfi')
process.load("Configuration.Geometry.GeometryExtended2021Reco_cff")
process.load("RecoJets.Configuration.CaloTowersES_cfi")

process.MessageLogger.cerr.FwkReport.reportEvery = 10000

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, '106X_mcRun3_2021_realistic_v3', '') # 106X 2021 MC
process.GlobalTag = GlobalTag(process.GlobalTag, '110X_mcRun3_2021_realistic_v6', '') # 110X 2021 MC

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                # dy 110X for test
                                #'/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/MINIAODSIM/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/250000/834F3FA5-E52E-4444-AFFD-F40FBA2DB9AA.root',
                                #'/store/mc/Run3Winter20DRMiniAOD/DYToLL_M-50_TuneCP5_14TeV-pythia8/MINIAODSIM/DRFlatPU30to80_110X_mcRun3_2021_realistic_v6-v2/250000/E33D7171-545A-5C47-949B-60EC752C12C7.root'

                                # double e pu 0
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_1.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_2.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_3.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_4.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_5.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_6.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_7.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_8.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_9.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_10.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_11.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_12.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_13.root',
                                #'/store/group/phys_egamma/afiqaize/DoubleEle-FlatPt2To250-PU0/DoubleEle-FlatPt2To250-PU0_13TeV-110X_mcRun3_2021_realistic_v6/MINIAODSIM/200226_172748/0000/test_14.root'
                            )
)

process.demo = cms.EDAnalyzer('FlatEleHoEAnalyzer',
                              electrons = cms.InputTag('slimmedElectrons'),
                              pileupCollection     = cms.InputTag("slimmedAddPileupInfo"),
                              hbheInput = cms.InputTag("reducedEgamma" ,  "reducedHBHEHits"),
                              ebReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedEBRecHits"),
                              eeReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedEERecHits"),
                              esReducedRecHitCollection = cms.InputTag("reducedEgamma", "reducedESRecHits"),
                              genParticleSrc       = cms.InputTag("prunedGenParticles"),
                              #genParticleSrc       = cms.InputTag("genParticles"),
                              Run2_2018_ = cms.bool(False),
                              rhoSrc = cms.InputTag("fixedGridRhoFastjetAll"),
                              genEventSrc = cms.InputTag("generator"),
                              output_file = cms.string('flat_electron.root')
)

process.p = cms.Path(process.demo)
