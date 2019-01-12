#/usr/share/texlive/texmf-dist/tex/generic 
#https://www.ctan.org/tex-archive/graphics/pstricks/contrib/
# https://www.ctan.org/pkg/bhcexam
# http://www.nongnu.org/fhsst/pstricks.html
# dsfont
# pst-fp　
# pst-tools

sudo apt-get install texlive-pstricks
# https://www.ctan.org/pkg/pstricks-base base.zip
sudo cp -R base/ /usr/share/texlive/texmf-dist/tex/generic
texhash
sudo cp -R pst-plot/ /usr/share/texlive/texmf-dist/tex/generic/
texhash
# https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tools
sudo cp -R pst-tools/ /usr/share/texlive/texmf-dist/tex/generic/
texhash
# https://www.ctan.org/pkg/pstricks-add
sudo cp -R pstricks-add/ /usr/share/texlive/texmf-dist/tex/generic/
texhash
# https://www.ctan.org/pkg/graphics
sudo cp -R graphics/ /usr/share/texlive/texmf-dist/tex/generic/
texhash
# https://www.ctan.org/pkg/bhcexam
sudo cp -R BHCexam/ /usr/share/texlive/texmf-dist/tex/generic/
texhash
# graphics/pstricks/contrib/pst-tools
# https://www.ctan.org/pkg/pst-fp
# Direc­tory graphics/pstricks/contrib/pst-node
# https://www.ctan.org/pkg/pstricks-base base.zip
# PSTricks of­fers an ex­ten­sive col­lec­tion of macros for gen­er­at­ing PostScript that is us­able with most TEX macro for­mats, in­clud­ing Plain TEX, LATEX, AMS-TEX, and AMS-LATEX. In­cluded are macros for colour, graph­ics, pie charts, ro­ta­tion, trees and over­lays. It has many spe­cial fea­tures, in­clud­ing a wide va­ri­ety of graph­ics (pic­ture draw­ing) macros, with a flex­i­ble in­ter­face and with colour sup­port. There are macros for colour­ing or shad­ing the cells of ta­bles.
