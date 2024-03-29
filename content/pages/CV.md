Title: CV/Bio
Authors: Eduardo Balbinot
Summary: My non-exhaustive CV
Sortorder: 2

## Short bio

I was born in Porto Alegre, the capital of the state of Rio Grande do Sul in
Brazil. I did my BSc (Physics), MSc (Astronomy), and PhD at Universidade
Federal do Rio Grande do Sul. During most of undergrad I was supervised by
Prof. Basilio Santiago and worked in a variety of topics such as globular
clusters, dwarf galaxies, stellar streams, and survey design and preparation.
After my PhD in 2014 I moved to a 4-year postdoctoral research position at the
University of Surrey (Guildford, UK), to work with Prof. Mark Gieles. There I
focussed mainly on the dynamics of globular clusters and dwarf galaxies,
heavily linked to large photometric/astrometric surveys. Since 2018 I have been
working on galactic archeology as a postdoc with Prof. Amina Helmi at the
Kapteyn Institute in the University of Groningen (NL). My main focus now is on
Gaia and near-future spectroscopic surveys, such as WEAVE and 4MOST.


## Curriculum vitae

My CV in <a href='/images/CV_EB.pdf'>PDF format</a>


My up-to-date ADS publication list can be found
[here](https://ui.adsabs.harvard.edu/search/filter_database_fq_database=OR&filter_database_fq_database=database%3A%22astronomy%22&format=SHORT&fq=%7B!type%3Daqp%20v%3D%24fq_database%7D&fq_database=(database%3A%22astronomy%22)&q=author%3A(%22balbinot%2C%20eduardo%22)&sort=score%20desc%2C%20bibcode%20desc&unprocessed_parameter=qform&unprocessed_parameter=adsobj_query&p_=0).
Alternatively, I made it available below using the following code:

<button id="slideToggleBtn">Click to see the code used to produce the publication list below</button><br><br>

<div id="div1", style='display:none'>

``` python
#!/usr/bin/env python
from astroquery import nasa_ads as na

with open('ads_token', 'r') as fin:
    tk = fin.read().strip()
    na.ADS.TOKEN = tk

na.ADS.NROWS = 200
na.ADS.SORT = 'asc bibcode'
na.ADS.ADS_FIELDS = ['author', 'title', 'pubdate', 'bibcode', 'citation_count',
                     'doctype', 'bibstem']
results = na.ADS.query_simple('Balbinot, Eduardo doctype:article')
results.sort(['pubdate'], reverse=True)

for n, (res) in enumerate(results):
    a = res['author']
    pd = res['pubdate']

    author_order = [i for i, s in enumerate(a) if 'Balbinot' in s]
    if author_order[0] > 9:
        auth = '; '.join(a[0:9]) + 'et al. with Balbinot, E'
    else:
        auth = '; '.join(a[0:8])

    auth = auth.replace('Balbinot, E.', '**Balbinot, E.**')
    auth = auth.replace('Balbinot, Eduardo', '**Balbinot, E.**')

    pyear = pd.split('-')[0]
    try:
        if pyear==opyear:
            pass
        else:
            print(f'### {pyear}')
            opyear=pyear
    except:
            opyear=pyear
            print(f'### {pyear}')
    url = f"https://ui.adsabs.harvard.edu/abs/{res['bibcode']}/abstract"

    print(f"{n+1}. [*{res['title'][0]}*]({url}){{:target='_blank'}} <br/> {auth} \
          ({res['bibstem'][0]}; {res['citation_count']} citations)")

```


</div><br>

It outputs the following:

## Publication List

### 2021
1. [*Variable stars in Local Group Galaxies - V. The fast and early evolution of the low-mass Eridanus II dSph galaxy*](https://ui.adsabs.harvard.edu/abs/2021MNRAS.tmp.2284M/abstract){:target='_blank'} <br/> Martínez-Vázquez, C. E.; Monelli, M.; Cassisi, S.; Taibi, S.; Gallart, C.; Vivas, A. K.; Walker, A. R.; Martín-Ravelo, P.; Zenteno, A.et al. with Balbinot, E           (MNRAS; 0 citations)
2. [*A supra-massive population of stellar-mass black holes in the globular cluster Palomar 5*](https://ui.adsabs.harvard.edu/abs/2021NatAs...5..957G/abstract){:target='_blank'} <br/> Gieles, Mark; Erkal, Denis; Antonini, Fabio; **Balbinot, E.**; Peñarrubia, Jorge           (NatAs; 7 citations)
3. [*Gaia Early Data Release 3. Summary of the contents and survey properties (Corrigendum)*](https://ui.adsabs.harvard.edu/abs/2021A&A...650C...3G/abstract){:target='_blank'} <br/> Gaia Collaboration; Brown, A. G. A.; Vallenari, A.; Prusti, T.; de Bruijne, J. H. J.; Babusiaux, C.; Biermann, M.; Creevey, O. L.; Evans, D. W.et al. with Balbinot, E           (A&A; 9 citations)
4. [*Gaia Early Data Release 3. Structure and properties of the Magellanic Clouds*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...7G/abstract){:target='_blank'} <br/> Gaia Collaboration; Luri, X.; Chemin, L.; Clementini, G.; Delgado, H. E.; McMillan, P. J.; Romero-Gómez, M.; **Balbinot, E.**           (A&A; 21 citations)
5. [*Gaia Early Data Release 3. Summary of the contents and survey properties*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...1G/abstract){:target='_blank'} <br/> Gaia Collaboration; Brown, A. G. A.; Vallenari, A.; Prusti, T.; de Bruijne, J. H. J.; Babusiaux, C.; Biermann, M.; Creevey, O. L.; Evans, D. W.et al. with Balbinot, E           (A&A; 552 citations)
6. [*MUSE narrow field mode observations of the central kinematics of M15*](https://ui.adsabs.harvard.edu/abs/2021MNRAS.503.1680U/abstract){:target='_blank'} <br/> Usher, Christopher; Kamann, Sebastian; Gieles, Mark; Hénault-Brunet, Vincent; Dalessandro, Emanuele; **Balbinot, E.**; Sollima, Antonio           (MNRAS; 4 citations)
7. [*Gaia Early Data Release 3. Catalogue validation*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...5F/abstract){:target='_blank'} <br/> Fabricius, C.; Luri, X.; Arenou, F.; Babusiaux, C.; Helmi, A.; Muraveva, T.; Reylé, C.; Spoto, F.; Vallenari, A.et al. with Balbinot, E           (A&A; 57 citations)
8. [*Gaia Early Data Release 3. The Gaia Catalogue of Nearby Stars*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...6G/abstract){:target='_blank'} <br/> Gaia Collaboration; Smart, R. L.; Sarro, L. M.; Rybizki, J.; Reylé, C.; Robin, A. C.; Hambly, N. C.; Abbas, U.; Barstow, M. A.et al. with Balbinot, E           (A&A; 49 citations)
9. [*Gaia Early Data Release 3. Acceleration of the Solar System from Gaia astrometry*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...9G/abstract){:target='_blank'} <br/> Gaia Collaboration; Klioner, S. A.; Mignard, F.; Lindegren, L.; Bastian, U.; McMillan, P. J.; Hernández, J.; Hobbs, D.; Ramos-Lerate, M.et al. with Balbinot, E           (A&A; 21 citations)
10. [*Gaia Early Data Release 3. The Galactic anticentre*](https://ui.adsabs.harvard.edu/abs/2021A&A...649A...8G/abstract){:target='_blank'} <br/> Gaia Collaboration; Antoja, T.; McMillan, P. J.; Kordopatis, G.; Ramos, P.; Helmi, A.; **Balbinot, E.**; Cantat-Gaudin, T.           (A&A; 11 citations)
11. [*The dynamics of the globular cluster NGC 3201 out to the Jacobi radius*](https://ui.adsabs.harvard.edu/abs/2021MNRAS.502.4513W/abstract){:target='_blank'} <br/> Wan, Zhen; Oliver, William H.; Baumgardt, Holger; Lewis, Geraint F.; Gieles, Mark; Hénault-Brunet, Vincent; de Boer, Thomas; **Balbinot, E.**           (MNRAS; 5 citations)
### 2020
12. [*Modelling the Milky Way - I. Method and first results fitting the thick disc and halo with DES-Y3 data*](https://ui.adsabs.harvard.edu/abs/2020MNRAS.497.1547P/abstract){:target='_blank'} <br/> Pieres, A.; Girardi, L.; **Balbinot, E.**; Santiago, B.; da Costa, L. N.; Carnero Rosell, A.; Pace, A. B.; Bechtol, K.           (MNRAS; 9 citations)
13. [*Full 5D characterisation of the Sagittarius stream with Gaia DR2 RR Lyrae (Corrigendum)*](https://ui.adsabs.harvard.edu/abs/2020A&A...640C...5R/abstract){:target='_blank'} <br/> Ramos, P.; Mateu, C.; Antoja, T.; Helmi, A.; Castro-Ginard, A.; **Balbinot, E.**; Carrasco, J. M.           (A&A; 0 citations)
14. [*The tidal remnant of an unusually metal-poor globular cluster*](https://ui.adsabs.harvard.edu/abs/2020Natur.583..768W/abstract){:target='_blank'} <br/> Wan, Zhen; Lewis, Geraint F.; Li, Ting S.; Simpson, Jeffrey D.; Martell, Sarah L.; Zucker, Daniel B.; Mould, Jeremy R.; Erkal, Denis; Pace, Andrew B.et al. with Balbinot, E           (Natur; 18 citations)
15. [*Full 5D characterisation of the Sagittarius stream with Gaia DR2 RR Lyrae*](https://ui.adsabs.harvard.edu/abs/2020A&A...638A.104R/abstract){:target='_blank'} <br/> Ramos, P.; Mateu, C.; Antoja, T.; Helmi, A.; Castro-Ginard, A.; **Balbinot, E.**; Carrasco, J. M.           (A&A; 22 citations)
16. [*On the black hole content and initial mass function of 47 Tuc*](https://ui.adsabs.harvard.edu/abs/2020MNRAS.491..113H/abstract){:target='_blank'} <br/> Hénault-Brunet, V.; Gieles, M.; Strader, J.; Peuten, M.; **Balbinot, E.**; Douglas, K. E. K.           (MNRAS; 17 citations)
### 2019
17. [*The southern stellar stream spectroscopic survey (S<SUP>5</SUP>): Overview, target selection, data reduction, validation, and early science*](https://ui.adsabs.harvard.edu/abs/2019MNRAS.490.3508L/abstract){:target='_blank'} <br/> Li, T. S.; Koposov, S. E.; Zucker, D. B.; Lewis, G. F.; Kuehn, K.; Simpson, J. D.; Ji, A. P.; Shipp, N.; Mao, Y. -Y.et al. with Balbinot, E           (MNRAS; 41 citations)
18. [*Globular cluster number density profiles using Gaia DR2*](https://ui.adsabs.harvard.edu/abs/2019MNRAS.485.4906D/abstract){:target='_blank'} <br/> de Boer, T. J. L.; Gieles, M.; **Balbinot, E.**; Hénault-Brunet, V.; Sollima, A.; Watkins, L. L.; Claydon, I.           (MNRAS; 36 citations)
19. [*A Search for Optical Emission from Binary Black Hole Merger GW170814 with the Dark Energy Camera*](https://ui.adsabs.harvard.edu/abs/2019ApJ...873L..24D/abstract){:target='_blank'} <br/> Doctor, Z.; Kessler, R.; Herner, K.; Palmese, A.; Soares-Santos, M.; Annis, J.; Brout, D.; Holz, D. E.; Sako, M.et al. with Balbinot, E           (ApJL; 13 citations)
20. [*4MOST: Project overview and information for the First Call for Proposals*](https://ui.adsabs.harvard.edu/abs/2019Msngr.175....3D/abstract){:target='_blank'} <br/> de Jong, R. S.; Agertz, O.; Berbel, A. A.; Aird, J.; Alexander, D. A.; Amarsi, A.; Anders, F.; Andrae, R.; Ansarinejad, B.et al. with Balbinot, E           (Msngr; 121 citations)
21. [*4MOST Consortium Survey 1: The Milky Way Halo Low-Resolution Survey*](https://ui.adsabs.harvard.edu/abs/2019Msngr.175...23H/abstract){:target='_blank'} <br/> Helmi, A.; Irwin, M.; Deason, A.; **Balbinot, E.**; Belokurov, V.; Bland-Hawthorn, J.; Christlieb, N.; Cioni, M. -R. L.           (Msngr; 9 citations)
22. [*Linking the rotation of a cluster to the spins of its stars: the kinematics of NGC 6791 and NGC 6819 in 3D*](https://ui.adsabs.harvard.edu/abs/2019MNRAS.483.2197K/abstract){:target='_blank'} <br/> Kamann, S.; Bastian, N. J.; Gieles, M.; **Balbinot, E.**; Hénault-Brunet, V.           (MNRAS; 10 citations)
### 2018
23. [*Star-galaxy classification in the Dark Energy Survey Y1 data set*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.481.5451S/abstract){:target='_blank'} <br/> Sevilla-Noarbe, I.; Hoyle, B.; Marchã, M. J.; Soumagnac, M. T.; Bechtol, K.; Drlica-Wagner, A.; Abdalla, F.; Aleksić, J.           (MNRAS; 22 citations)
24. [*Modelling the Tucana III stream - a close passage with the LMC*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.481.3148E/abstract){:target='_blank'} <br/> Erkal, D.; Li, T. S.; Koposov, S. E.; Belokurov, V.; **Balbinot, E.**; Bechtol, K.; Buncher, B.; Drlica-Wagner, A.           (MNRAS; 43 citations)
25. [*The First Tidally Disrupted Ultra-faint Dwarf Galaxy?: A Spectroscopic Analysis of the Tucana III Stream*](https://ui.adsabs.harvard.edu/abs/2018ApJ...866...22L/abstract){:target='_blank'} <br/> Li, T. S.; Simon, J. D.; Kuehn, K.; Pace, A. B.; Erkal, D.; Bechtol, K.; Yanny, B.; Drlica-Wagner, A.; Marshall, J. L.et al. with Balbinot, E           (ApJ; 44 citations)
26. [*Stellar Streams Discovered in the Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2018ApJ...862..114S/abstract){:target='_blank'} <br/> Shipp, N.; Drlica-Wagner, A.; **Balbinot, E.**; Ferguson, P.; Erkal, D.; Li, T. S.; Bechtol, K.; Belokurov, V.           (ApJ; 134 citations)
27. [*Dark Energy Survey year 1 results: Cosmological constraints from galaxy clustering and weak lensing*](https://ui.adsabs.harvard.edu/abs/2018PhRvD..98d3526A/abstract){:target='_blank'} <br/> Abbott, T. M. C.; Abdalla, F. B.; Alarcon, A.; Aleksić, J.; Allam, S.; Allen, S.; Amara, A.; Annis, J.; Asorey, J.et al. with Balbinot, E           (PhRvD; 769 citations)
28. [*Deep SOAR follow-up photometry of two Milky Way outer-halo companions discovered with Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.478.2006L/abstract){:target='_blank'} <br/> Luque, E.; Santiago, B.; Pieres, A.; Marshall, J. L.; Pace, A. B.; Kron, R.; Drlica-Wagner, A.; Queiroz, A.           (MNRAS; 11 citations)
29. [*Probing dark matter with star clusters: a dark matter core in the ultra-faint dwarf Eridanus II*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.476.3124C/abstract){:target='_blank'} <br/> Contenta, Filippo; **Balbinot, E.**; Petts, James A.; Read, Justin I.; Gieles, Mark; Collins, Michelle L. M.; Peñarrubia, Jorge; Delorme, Maxime           (MNRAS; 32 citations)
30. [*Mass models of NGC 6624 without an intermediate-mass black hole*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.4832G/abstract){:target='_blank'} <br/> Gieles, Mark; **Balbinot, E.**; Yaaqib, Rashid I. S. M.; Hénault-Brunet, Vincent; Zocchi, Alice; Peuten, Miklos; Jonker, Peter G.           (MNRAS; 35 citations)
31. [*The devil is in the tails: the role of globular cluster mass evolution on stream properties*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.474.2479B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Gieles, Mark           (MNRAS; 61 citations)
32. [*Chemical Abundance Analysis of Three α-poor, Metal-poor Stars in the Ultrafaint Dwarf Galaxy Horologium I*](https://ui.adsabs.harvard.edu/abs/2018ApJ...852...99N/abstract){:target='_blank'} <br/> Nagasawa, D. Q.; Marshall, J. L.; Li, T. S.; Hansen, T. T.; Simon, J. D.; Bernstein, R. A.; **Balbinot, E.**; Drlica-Wagner, A.           (ApJ; 23 citations)
33. [*Cartography of Triangulum-Andromeda using SDSS stars*](https://ui.adsabs.harvard.edu/abs/2018MNRAS.473.1461P/abstract){:target='_blank'} <br/> Perottoni, H. D.; Rocha-Pinto, H. J.; Girardi, L.; **Balbinot, E.**; Santiago, B. X.; Majewski, S. R.; Anders, F.; Da Costa, L.           (MNRAS; 8 citations)
### 2017
34. [*A gravitational-wave standard siren measurement of the Hubble constant*](https://ui.adsabs.harvard.edu/abs/2017Natur.551...85A/abstract){:target='_blank'} <br/> Abbott, B. P.; Abbott, R.; Abbott, T. D.; Acernese, F.; Ackley, K.; Adams, C.; Adams, T.; Addesso, P.; Adhikari, R. X.et al. with Balbinot, E           (Natur; 576 citations)
35. [*The Electromagnetic Counterpart of the Binary Neutron Star Merger LIGO/Virgo GW170817. I. Discovery of the Optical Counterpart Using the Dark Energy Camera*](https://ui.adsabs.harvard.edu/abs/2017ApJ...848L..16S/abstract){:target='_blank'} <br/> Soares-Santos, M.; Holz, D. E.; Annis, J.; Chornock, R.; Herner, K.; Berger, E.; Brout, D.; Chen, H. -Y.; Kessler, R.et al. with Balbinot, E           (ApJL; 309 citations)
36. [*The Electromagnetic Counterpart of the Binary Neutron Star Merger LIGO/Virgo GW170817. II. UV, Optical, and Near-infrared Light Curves and Comparison to Kilonova Models*](https://ui.adsabs.harvard.edu/abs/2017ApJ...848L..17C/abstract){:target='_blank'} <br/> Cowperthwaite, P. S.; Berger, E.; Villar, V. A.; Metzger, B. D.; Nicholl, M.; Chornock, R.; Blanchard, P. K.; Fong, W.; Margutti, R.et al. with Balbinot, E           (ApJL; 482 citations)
37. [*Multi-messenger Observations of a Binary Neutron Star Merger*](https://ui.adsabs.harvard.edu/abs/2017ApJ...848L..12A/abstract){:target='_blank'} <br/> Abbott, B. P.; Abbott, R.; Abbott, T. D.; Acernese, F.; Ackley, K.; Adams, C.; Adams, T.; Addesso, P.; Adhikari, R. X.et al. with Balbinot, E           (ApJL; 2013 citations)
38. [*The Dark Energy Survey view of the Sagittarius stream: discovery of two faint stellar system candidates*](https://ui.adsabs.harvard.edu/abs/2017MNRAS.468...97L/abstract){:target='_blank'} <br/> Luque, E.; Pieres, A.; Santiago, B.; Yanny, B.; Vivas, A. K.; Queiroz, A.; Drlica-Wagner, A.; Morganson, E.           (MNRAS; 34 citations)
39. [*A stellar overdensity associated with the Small Magellanic Cloud*](https://ui.adsabs.harvard.edu/abs/2017MNRAS.468.1349P/abstract){:target='_blank'} <br/> Pieres, A.; Santiago, B. X.; Drlica-Wagner, A.; Bechtol, K.; Marel, R. P. van der; Besla, G.; Martin, N. F.; Belokurov, V.; Gallart, C.et al. with Balbinot, E           (MNRAS; 30 citations)
40. [*The contribution of dissolving star clusters to the population of ultra faint objects in the outer halo of the Milky Way*](https://ui.adsabs.harvard.edu/abs/2017MNRAS.466.1741C/abstract){:target='_blank'} <br/> Contenta, Filippo; Gieles, Mark; **Balbinot, E.**; Collins, Michelle L. M.           (MNRAS; 14 citations)
41. [*Nearest Neighbor: The Low-mass Milky Way Satellite Tucana III*](https://ui.adsabs.harvard.edu/abs/2017ApJ...838...11S/abstract){:target='_blank'} <br/> Simon, J. D.; Li, T. S.; Drlica-Wagner, A.; Bechtol, K.; Marshall, J. L.; James, D. J.; Wang, M. Y.; Strigari, L.           (ApJ; 73 citations)
42. [*Differences in the rotational properties of multiple stellar populations in M13: a faster rotation for the `extreme' chemical subpopulation*](https://ui.adsabs.harvard.edu/abs/2017MNRAS.465.3515C/abstract){:target='_blank'} <br/> Cordero, M. J.; Hénault-Brunet, V.; Pilachowski, C. A.; **Balbinot, E.**; Johnson, C. I.; Varri, A. L.           (MNRAS; 45 citations)
43. [*Farthest Neighbor: The Distant Milky Way Satellite Eridanus II*](https://ui.adsabs.harvard.edu/abs/2017ApJ...838....8L/abstract){:target='_blank'} <br/> Li, T. S.; Simon, J. D.; Drlica-Wagner, A.; Bechtol, K.; Wang, M. Y.; García-Bellido, J.; Frieman, J.; Marshall, J. L.; James, D. J.et al. with Balbinot, E           (ApJ; 109 citations)
### 2016
44. [*Physical properties of star clusters in the outer LMC as observed by the DES*](https://ui.adsabs.harvard.edu/abs/2016MNRAS.461..519P/abstract){:target='_blank'} <br/> Pieres, A.; Santiago, B.; **Balbinot, E.**; Luque, E.; Queiroz, A.; da Costa, L. N.; Maia, M. A. G.; Drlica-Wagner, A.           (MNRAS; 21 citations)
45. [*Noble gas composition of subcontinental lithospheric mantle: An extensively degassed reservoir beneath Southern Patagonia*](https://ui.adsabs.harvard.edu/abs/2016E&PSL.450..263J/abstract){:target='_blank'} <br/> Jalowitzki, Tiago; Sumino, Hirochika; Conceição, Rommulo V.; Orihashi, Yuji; Nagao, Keisuke; Bertotto, Gustavo W.; **Balbinot, E.**; Schilling, Manuel E.           (E&PSL; 8 citations)
46. [*The Dark Energy Survey: more than dark energy - an overview*](https://ui.adsabs.harvard.edu/abs/2016MNRAS.460.1270D/abstract){:target='_blank'} <br/> Dark Energy Survey Collaboration; Abbott, T.; Abdalla, F. B.; Aleksić, J.; Allam, S.; Amara, A.; Bacon, D.; **Balbinot, E.**           (MNRAS; 481 citations)
47. [*No evidence for younger stellar generations within the intermediate-age massive clusters NGC 1783, NGC 1806 and NGC 411*](https://ui.adsabs.harvard.edu/abs/2016MNRAS.459.4218C/abstract){:target='_blank'} <br/> Cabrera-Ziri, I.; Niederhofer, F.; Bastian, N.; Rejkuba, M.; **Balbinot, E.**; Kerzendorf, W. E.; Larsen, S. S.; Mackey, A. D.           (MNRAS; 15 citations)
48. [*Digging deeper into the Southern skies: a compact Milky Way companion discovered in first-year Dark Energy Survey data*](https://ui.adsabs.harvard.edu/abs/2016MNRAS.458..603L/abstract){:target='_blank'} <br/> Luque, E.; Queiroz, A.; Santiago, B.; Pieres, A.; **Balbinot, E.**; Bechtol, K.; Drlica-Wagner, A.; Neto, A. Fausti           (MNRAS; 49 citations)
49. [*The Phoenix Stream: A Cold Stream in the Southern Hemisphere*](https://ui.adsabs.harvard.edu/abs/2016ApJ...820...58B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Yanny, B.; Li, T. S.; Santiago, B.; Marshall, J. L.; Finley, D. A.; Pieres, A.; Abbott, T. M. C.           (ApJ; 41 citations)
50. [*Discovery of a Stellar Overdensity in Eridanus-Phoenix in the Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2016ApJ...817..135L/abstract){:target='_blank'} <br/> Li, T. S.; **Balbinot, E.**; Mondrik, N.; Marshall, J. L.; Yanny, B.; Bechtol, K.; Drlica-Wagner, A.; Oscar, D.           (ApJ; 27 citations)
51. [*Spectro-photometric distances to stars: A general purpose Bayesian approach*](https://ui.adsabs.harvard.edu/abs/2016A&A...585A..42S/abstract){:target='_blank'} <br/> Santiago, Basílio X.; Brauer, Dorothée E.; Anders, Friedrich; Chiappini, Cristina; Queiroz, Anna B.; Girardi, Léo; Rocha-Pinto, Helio J.; **Balbinot, E.**           (A&A; 59 citations)
### 2015
52. [*Bridge over troubled gas: clusters and associations under the SMC and LMC tidal stresses*](https://ui.adsabs.harvard.edu/abs/2015MNRAS.453.3190B/abstract){:target='_blank'} <br/> Bica, E.; Santiago, B.; Bonatto, C.; Garcia-Dias, R.; Kerber, L.; Dias, B.; Barbuy, B.; **Balbinot, E.**           (MNRAS; 18 citations)
53. [*Eight Ultra-faint Galaxy Candidates Discovered in Year Two of the Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2015ApJ...813..109D/abstract){:target='_blank'} <br/> Drlica-Wagner, A.; Bechtol, K.; Rykoff, E. S.; Luque, E.; Queiroz, A.; Mao, Y. -Y.; Wechsler, R. H.; Simon, J. D.; Santiago, B.et al. with Balbinot, E           (ApJ; 345 citations)
54. [*Biases in the determination of dynamical parameters of star clusters: today and in the Gaia era*](https://ui.adsabs.harvard.edu/abs/2015MNRAS.451.2185S/abstract){:target='_blank'} <br/> Sollima, A.; Baumgardt, H.; Zocchi, A.; **Balbinot, E.**; Gieles, M.; Hénault-Brunet, V.; Varri, A. L.           (MNRAS; 32 citations)
55. [*Search for Gamma-Ray Emission from DES Dwarf Spheroidal Galaxy Candidates with Fermi-LAT Data*](https://ui.adsabs.harvard.edu/abs/2015ApJ...809L...4D/abstract){:target='_blank'} <br/> Drlica-Wagner, A.; Albert, A.; Bechtol, K.; Wood, M.; Strigari, L.; Sánchez-Conde, M.; Baldini, L.; Essig, R.; Cohen-Tanugi, J.et al. with Balbinot, E           (ApJL; 162 citations)
56. [*Eight New Milky Way Companions Discovered in First-year Dark Energy Survey Data*](https://ui.adsabs.harvard.edu/abs/2015ApJ...807...50B/abstract){:target='_blank'} <br/> Bechtol, K.; Drlica-Wagner, A.; **Balbinot, E.**; Pieres, A.; Simon, J. D.; Yanny, B.; Santiago, B.; Wechsler, R. H.           (ApJ; 422 citations)
57. [*Stellar Kinematics and Metallicities in the Ultra-faint Dwarf Galaxy Reticulum II*](https://ui.adsabs.harvard.edu/abs/2015ApJ...808...95S/abstract){:target='_blank'} <br/> Simon, J. D.; Drlica-Wagner, A.; Li, T. S.; Nord, B.; Geha, M.; Bechtol, K.; **Balbinot, E.**; Buckley-Geer, E.           (ApJ; 119 citations)
58. [*The LMC geometry and outer stellar populations from early DES data*](https://ui.adsabs.harvard.edu/abs/2015MNRAS.449.1129B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Santiago, B. X.; Girardi, L.; Pieres, A.; da Costa, L. N.; Maia, M. A. G.; Gruendl, R. A.; Walker, A. R.           (MNRAS; 36 citations)
59. [*Globular Cluster Streams as Galactic High-Precision Scales—the Poster Child Palomar 5*](https://ui.adsabs.harvard.edu/abs/2015ApJ...803...80K/abstract){:target='_blank'} <br/> Küpper, Andreas H. W.; **Balbinot, E.**; Bonaca, Ana; Johnston, Kathryn V.; Hogg, David W.; Kroupa, Pavel; Santiago, Basilio X.           (ApJ; 133 citations)
60. [*Modeling the Transfer Function for the Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2015ApJ...801...73C/abstract){:target='_blank'} <br/> Chang, C.; Busha, M. T.; Wechsler, R. H.; Refregier, A.; Amara, A.; Rykoff, E.; Becker, M. R.; Bruderer, C.; Gamper, L.et al. with Balbinot, E           (ApJ; 33 citations)
### 2014
61. [*Chemodynamics of the Milky Way. I. The first year of APOGEE data*](https://ui.adsabs.harvard.edu/abs/2014A&A...564A.115A/abstract){:target='_blank'} <br/> Anders, F.; Chiappini, C.; Santiago, B. X.; Rocha-Pinto, H. J.; Girardi, L.; da Costa, L. N.; Maia, M. A. G.; Steinmetz, M.; Minchev, I.et al. with Balbinot, E           (A&A; 155 citations)
62. [*Self-consistent physical parameters for five intermediate-age SMC stellar clusters from CMD modelling*](https://ui.adsabs.harvard.edu/abs/2014A&A...561A.106D/abstract){:target='_blank'} <br/> Dias, B.; Kerber, L. O.; Barbuy, B.; Santiago, B.; Ortolani, S.; **Balbinot, E.**           (A&A; 18 citations)
### 2013
63. [*A New Milky Way Halo Star Cluster in the Southern Galactic Sky*](https://ui.adsabs.harvard.edu/abs/2013ApJ...767..101B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Santiago, B. X.; da Costa, L.; Maia, M. A. G.; Majewski, S. R.; Nidever, D.; Rocha-Pinto, H. J.; Thomas, D.           (ApJ; 44 citations)
64. [*PreCam: A Precursor Observational Campaign for Calibration of the Dark Energy Survey*](https://ui.adsabs.harvard.edu/abs/2013PASP..125..409K/abstract){:target='_blank'} <br/> Kuehn, K.; Kuhlmann, S.; Allam, S.; Annis, J. T.; Bailey, T.; **Balbinot, E.**; Bernstein, J. P.; Biesiadzinski, T.           (PASP; 3 citations)
### 2012
65. [*The Ninth Data Release of the Sloan Digital Sky Survey: First Spectroscopic Data from the SDSS-III Baryon Oscillation Spectroscopic Survey*](https://ui.adsabs.harvard.edu/abs/2012ApJS..203...21A/abstract){:target='_blank'} <br/> Ahn, Christopher P.; Alexandroff, Rachael; Allende Prieto, Carlos; Anderson, Scott F.; Anderton, Timothy; Andrews, Brett H.; Aubourg, Éric; Bailey, Stephen           (ApJS; 1087 citations)
### 2011
66. [*The tidal tails of NGC 2298*](https://ui.adsabs.harvard.edu/abs/2011MNRAS.416..393B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Santiago, Basílio X.; da Costa, Luiz N.; Makler, Martin; Maia, Marcio A. G.           (MNRAS; 30 citations)
67. [*SDSS-III: Massive Spectroscopic Surveys of the Distant Universe, the Milky Way, and Extra-Solar Planetary Systems*](https://ui.adsabs.harvard.edu/abs/2011AJ....142...72E/abstract){:target='_blank'} <br/> Eisenstein, Daniel J.; Weinberg, David H.; Agol, Eric; Aihara, Hiroaki; Allende Prieto, Carlos; Anderson, Scott F.; Arns, James A.; Aubourg, Éric           (AJ; 1553 citations)
68. [*The Dark Energy Survey: Prospects for Resolved Stellar Populations*](https://ui.adsabs.harvard.edu/abs/2011AJ....141..185R/abstract){:target='_blank'} <br/> Rossetto, Bruno M.; Santiago, Basílio X.; Girardi, Léo; Camargo, Julio I. B.; **Balbinot, E.**; da Costa, Luiz N.; Yanny, Brian; Maia, Marcio A. G.           (AJ; 21 citations)
69. [*The Eighth Data Release of the Sloan Digital Sky Survey: First Data from SDSS-III*](https://ui.adsabs.harvard.edu/abs/2011ApJS..193...29A/abstract){:target='_blank'} <br/> Aihara, Hiroaki; Allende Prieto, Carlos; An, Deokkeun; Anderson, Scott F.; Aubourg, Éric; **Balbinot, E.**; Beers, Timothy C.; Berlind, Andreas A.           (ApJS; 1101 citations)
70. [*Panchromatic averaged stellar populations*](https://ui.adsabs.harvard.edu/abs/2011MNRAS.411.1897R/abstract){:target='_blank'} <br/> Riffel, R.; Bonatto, C.; Cid Fernandes, R.; Pastoriza, M. G.; **Balbinot, E.**           (MNRAS; 8 citations)
### 2010
71. [*Probing the Large Magellanic Cloud age gap at intermediate cluster masses*](https://ui.adsabs.harvard.edu/abs/2010MNRAS.404.1625B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Santiago, B. X.; Kerber, L. O.; Barbuy, B.; Dias, B. M. S.           (MNRAS; 12 citations)
### 2009
72. [*The globular cluster NGC 6642: evidence for a depleted mass function in a very old cluster*](https://ui.adsabs.harvard.edu/abs/2009MNRAS.396.1596B/abstract){:target='_blank'} <br/> **Balbinot, E.**; Santiago, B. X.; Bica, E.; Bonatto, C.           (MNRAS; 14 citations)
