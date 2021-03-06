"""LSST-specific overrides for MultiBandTask"""

import os.path

from lsst.utils import getPackageDir

for sub in ("mergeCoaddDetections", "measureCoaddSources", "mergeCoaddMeasurements", "forcedPhotCoadd"):
    path = os.path.join(getPackageDir("obs_lsst"), "config", sub + ".py")
    if os.path.exists(path):
        getattr(config, sub).load(path)
