"""   -- Start License block
        JCR6zlib.py
	(c) 2016 Jeroen Petrus Broks.
	
	This Source Code Form is subject to the terms of the 
	Mozilla Public License, v. 2.0. If a copy of the MPL was not 
	distributed with this file, You can obtain one at 
	http://mozilla.org/MPL/2.0/.
        Version: 16.03.12
       -- End License block   """
import JCR6
import zlib

class jcrzlib:
      def STORE(self,s): return zlib.compress(s)
      def RESTORE(self,s): return zlib.decompress(s)
	
JCR6.Storages['zlib'] = jcrzlib()	
