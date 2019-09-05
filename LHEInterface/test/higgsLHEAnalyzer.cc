#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Run.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "FWCore/Utilities/interface/EDMException.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "TLorentzVector.h"

#include <iomanip>
#include <iostream>
using namespace std;
using namespace edm;
using namespace lhef;

class higgsLHEAnalyzer : public EDAnalyzer {
private: 
  bool dumpLHE_;
  bool checkPDG_;
  TH1F * h_hMass;
  TH1F * h_Mass;
  TH1F * h_longMass;
  TH1F * h_diEMass;
  TH1F * h_diMuMass;
  int id6, id7;
public:
  explicit higgsLHEAnalyzer( const ParameterSet & cfg ) : 
    src_( cfg.getParameter<InputTag>( "src" ) ),
    tokenLHERunInfo_(consumes<LHERunInfoProduct,edm::InRun>(cfg.getUntrackedParameter<edm::InputTag>("moduleLabel", std::string("source")) ) ),
    tokenLHEEvent_(consumes<LHEEventProduct>(cfg.getUntrackedParameter<edm::InputTag>("moduleLabel", std::string("source")) ) )
  {
    edm::Service<TFileService> fs;
    h_hMass    = fs->make<TH1F>( "h_hMass"  , "mh", 50,  95, 155 );
    h_Mass    = fs->make<TH1F>( "h_Mass"  , "mll", 50,  0, 1 );
    h_diEMass    = fs->make<TH1F>( "h_diEMass"  , "mll", 50,  0, 1 );
    h_diMuMass    = fs->make<TH1F>( "h_diMuMass"  , "mll", 50,  0, 1 );
    h_longMass    = fs->make<TH1F>( "h_longMass"  , "mll", 100,  0, 100 );
    //h_eta   = fs->make<TH1F>( "eta" , "#eta" , 50, -3, 3 );
  }
private:
  void analyze( const Event & iEvent, const EventSetup & iSetup ) override {

    edm::Handle<LHEEventProduct> evt;
    //iEvent.getByLabel(src_, evt);
    iEvent.getByToken(tokenLHEEvent_, evt);

    TLorentzVector l1_tlov4;
    TLorentzVector l2_tlov4;
    TLorentzVector diLep_tlov4;
    const lhef::HEPEUP hepeup_ = evt->hepeup();

    const int nup_ = hepeup_.NUP; 
    const std::vector<int> idup_ = hepeup_.IDUP;
    const std::vector<lhef::HEPEUP::FiveVector> pup_ = hepeup_.PUP;

    std::cout << "Number of particles = " << nup_ << std::endl;

    if ( evt->pdf() != NULL ) {
      std::cout << "PDF scale = " << std::setw(14) << std::fixed << evt->pdf()->scalePDF << std::endl;  
      std::cout << "PDF 1 : id = " << std::setw(14) << std::fixed << evt->pdf()->id.first 
                << " x = " << std::setw(14) << std::fixed << evt->pdf()->x.first 
                << " xPDF = " << std::setw(14) << std::fixed << evt->pdf()->xPDF.first << std::endl;  
      std::cout << "PDF 2 : id = " << std::setw(14) << std::fixed << evt->pdf()->id.second 
                << " x = " << std::setw(14) << std::fixed << evt->pdf()->x.second 
                << " xPDF = " << std::setw(14) << std::fixed << evt->pdf()->xPDF.second << std::endl;  
    }

    for ( unsigned int icount = 0 ; icount < (unsigned int)nup_; icount++ ) {

      //std::cout << "# " << std::setw(14) << std::fixed << icount 
      //          << std::setw(14) << std::fixed << idup_[icount] 
      //          << std::setw(14) << std::fixed << hepeup_.ISTUP.at(icount)
      //          << std::setw(14) << std::fixed << (pup_[icount])[0]  //px
      //          << std::setw(14) << std::fixed << (pup_[icount])[1]  //py
      //          << std::setw(14) << std::fixed << (pup_[icount])[2]  //pz
      //          << std::setw(14) << std::fixed << (pup_[icount])[3]  //e
      //          << std::setw(14) << std::fixed << (pup_[icount])[4]  //mass
      //          << std::endl;
      //if(icount == 6 || icount == 7){
      //  if(hepeup_.ISTUP.at(icount) !=1) exit(-1);
      //  std::cout << "# " << std::setw(14) << std::fixed << icount
      //    << std::setw(14) << std::fixed << idup_[icount]
      //    << std::setw(14) << std::fixed << hepeup_.ISTUP.at(icount)
      //    << std::setw(14) << std::fixed << (pup_[icount])[0]  //px
      //    << std::setw(14) << std::fixed << (pup_[icount])[1]  //py
      //    << std::setw(14) << std::fixed << (pup_[icount])[2]  //pz
      //    << std::setw(14) << std::fixed << (pup_[icount])[3]  //e
      //    << std::setw(14) << std::fixed << (pup_[icount])[4]  //mass
      //    << std::endl;

      //}
      //
      if(icount == 6 ){
	id6=idup_[icount];
	l1_tlov4.SetPxPyPzE((pup_[icount])[0] ,(pup_[icount])[1],(pup_[icount])[2],(pup_[icount])[3] );
      }
      if(icount == 7 ){
	id7=idup_[icount];
	l2_tlov4.SetPxPyPzE((pup_[icount])[0] ,(pup_[icount])[1],(pup_[icount])[2],(pup_[icount])[3] );
      }
      //if(idup_[icount] == 23 ){
      if(idup_[icount] == 25 ){
	h_hMass->Fill((pup_[icount])[4]); 
      }
    }
    diLep_tlov4 = l1_tlov4+l2_tlov4;
    //std::cout<<std::setw(14) << diLep_tlov4.M()  //mass
     // << std::endl;
    h_Mass->Fill(diLep_tlov4.M()); 
    h_longMass->Fill(diLep_tlov4.M()); 
    if(id6*id7 == -11*11) h_diEMass->Fill(diLep_tlov4.M());
    if(id6*id7 == -13*13) h_diMuMass->Fill(diLep_tlov4.M());


    //if( evt->weights().size() ) {
    //  std::cout << "weights:" << std::endl;
    //  for ( size_t iwgt = 0; iwgt < evt->weights().size(); ++iwgt ) {
    //    const LHEEventProduct::WGT& wgt = evt->weights().at(iwgt);
    //    std::cout << "\t" << wgt.id << ' ' 
    //    	  << std::scientific << wgt.wgt << std::endl;
    //  }
    //}

  }

  void endRun(edm::Run const& iRun, edm::EventSetup const& es) override {

    Handle<LHERunInfoProduct> run;
    //iRun.getByLabel( src_, run );
    iRun.getByToken( tokenLHERunInfo_, run );

    const lhef::HEPRUP thisHeprup_ = run->heprup();

    std::cout << "HEPRUP \n" << std::endl;
    std::cout << "IDBMUP " << std::setw(14) << std::fixed << thisHeprup_.IDBMUP.first 
              << std::setw(14) << std::fixed << thisHeprup_.IDBMUP.second << std::endl; 
    std::cout << "EBMUP  " << std::setw(14) << std::fixed << thisHeprup_.EBMUP.first 
              << std::setw(14) << std::fixed << thisHeprup_.EBMUP.second << std::endl; 
    std::cout << "PDFGUP " << std::setw(14) << std::fixed << thisHeprup_.PDFGUP.first 
              << std::setw(14) << std::fixed << thisHeprup_.PDFGUP.second << std::endl; 
    std::cout << "PDFSUP " << std::setw(14) << std::fixed << thisHeprup_.PDFSUP.first 
              << std::setw(14) << std::fixed << thisHeprup_.PDFSUP.second << std::endl; 
    std::cout << "IDWTUP " << std::setw(14) << std::fixed << thisHeprup_.IDWTUP << std::endl; 
    std::cout << "NPRUP  " << std::setw(14) << std::fixed << thisHeprup_.NPRUP << std::endl; 
    std::cout << "        XSECUP " << std::setw(14) << std::fixed 
              << "        XERRUP " << std::setw(14) << std::fixed 
              << "        XMAXUP " << std::setw(14) << std::fixed 
              << "        LPRUP  " << std::setw(14) << std::fixed << std::endl;
    for ( unsigned int iSize = 0 ; iSize < thisHeprup_.XSECUP.size() ; iSize++ ) {
      std::cout  << std::setw(14) << std::fixed << thisHeprup_.XSECUP[iSize]
                 << std::setw(14) << std::fixed << thisHeprup_.XERRUP[iSize]
                 << std::setw(14) << std::fixed << thisHeprup_.XMAXUP[iSize]
                 << std::setw(14) << std::fixed << thisHeprup_.LPRUP[iSize] 
                 << std::endl;
    }
    std::cout << " " << std::endl;

  }

  InputTag src_;
  edm::EDGetTokenT<LHERunInfoProduct> tokenLHERunInfo_;
  edm::EDGetTokenT<LHEEventProduct> tokenLHEEvent_;

};

#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE( higgsLHEAnalyzer );


