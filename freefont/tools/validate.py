#!/usr/local/bin/fontforge -script 
"""
Runs the FontForge validate function on all the font faces.
Prints report on standard output.
Returns 1 if problems found 0 otherwise.
"""
__author__ = "Stevan White <stevan.white@googlemail.com>"

import fontforge
import sys

problem = False


""" Haven't really figured out why TT limit warniings are turndd on,
	or where the limits are set.
"""
def countPointsInLayer( layer ):
	problem = True
	p = 0
	for c in layer:
		p += len( c )
	return p

def printProblemLine( e, msg ):
	print "\t" + e.glyphname + msg 

def dealWithValidationState( state, e ):
	if state & 0x2:
		printProblemLine( e, " has open contour" )
	if state & 0x4:
		printProblemLine( e, " intersects itself" )
	if state & 0x8:
		printProblemLine( e, " is drawn in wrong direction" )
	if state & 0x10:
		printProblemLine( e, " has a flipped reference" )
	if state & 0x20:
		printProblemLine( e, " is missing extrema" )
	if state & 0x40:
		printProblemLine( e, " is missing a reference in a table" )
	if state & 0x80:
		printProblemLine( e, " has more than 1500 pts" )
	if state & 0x100:
		printProblemLine( e, " has more than 96 hints" )
	if state & 0x200:
		printProblemLine( e, " has invalid PS name" )
	"""
	# Not meaningfully set for non-TrueType fonts )
	if state & 0x400:
		printProblemLine( e, " has more points than allowed by TT: " + str( countPointsInLayer( e.layers[1] ) ) )
	if state & 0x800:
		printProblemLine( e, " has more paths than allowed by TT" )
	if state & 0x1000:
		printProblemLine( e, " has more points in composite than allowed by TT" )
	if state & 0x2000:
		printProblemLine( e, " has more paths in composite than allowed by TT" )
	if state & 0x4000:
		printProblemLine( e, " has instruction longer than allowed" )
	if state & 0x8000:
		printProblemLine( e, " has more references than allowed" )
	if state & 0x10000:
		printProblemLine( e, " has references deeper than allowed" )
	if state & 0x20000:
		print e.glyphname + " fpgm or prep tables longer than allowed" )
	"""

def validate( fontPath ):
	print "Validating " + fontPath
	font = fontforge.open( fontPath )

	g = font.selection.all()
	g = font.selection.byGlyphs

	valid = True
	for e in g:
		state = e.validate()
		if state != 0:
			dealWithValidationState( state, e )
	font.validate
#validate( '../sfd/FreeSerif.sfd' )
validate( '../sfd/FreeSerifItalic.sfd' )
validate( '../sfd/FreeSerifBold.sfd' )
validate( '../sfd/FreeSerifBoldItalic.sfd' )
validate( '../sfd/FreeSans.sfd' )
validate( '../sfd/FreeSansOblique.sfd' )
validate( '../sfd/FreeSansBold.sfd' )
validate( '../sfd/FreeSansBoldOblique.sfd' )
validate( '../sfd/FreeMono.sfd' )
validate( '../sfd/FreeMonoOblique.sfd' )
validate( '../sfd/FreeMonoBold.sfd' )
validate( '../sfd/FreeMonoBoldOblique.sfd' )

if problem:
	sys.exit( 1 )
