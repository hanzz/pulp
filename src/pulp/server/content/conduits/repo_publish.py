# -*- coding: utf-8 -*-
#
# Copyright © 2011 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

"""
Contains the definitions for all classes related to the distributor's API for
interacting with the Pulp server during a repo publish.
"""

from gettext import gettext as _
import logging
import os
import sys

# -- constants ---------------------------------------------------------------

_LOG = logging.getLogger(__name__)

# -- exceptions --------------------------------------------------------------

class RepoPublishConduitException(Exception):
    """
    General exception that wraps any server exception coming out of a conduit
    call.
    """
    pass

# -- classes -----------------------------------------------------------------

class RepoPublishConduit:
    """
    Used to communicate back into the Pulp server while a distributor is
    publishing a repo. Instances of this call should *not* be cached between
    repo publish runs. Each publish call will be issued its own conduit
    instance that is scoped to that run alone.

    Instances of this class are thread-safe. The distributor implementation is
    allowed to do whatever threading makes sense to optimize the publishing.
    Calls into this instance do not have to be coordinated for thread safety,
    the instance will take care of it itself.
    """

    def __init__(self, repo_id, distributor_id, progress_callback=None):
        """
        @param repo_id: identifies the repo being published
        @type  repo_id: str

        @param distributor_id: identifies the distributor being published
        @type  distributor_id: str

        @param progress_callback: used to update the server's knowledge of the
                                  publish progress
        @type  progress_callback: ?
        """
        self.repo_id = repo_id
        self.distributor_id = distributor_id
        
        self.__progress_callback = progress_callback

    def __str__(self):
        return _('RepoPublishConduit for repository [%(r)s]' % {'r' : self.repo_id})

    # -- public ---------------------------------------------------------------

    def last_publish(self):
        """
        Returns the timestamp of the last time this repo was published,
        regardless of the success or failure of the publish. If
        the repo was never published, this call returns None.

        @return: timestamp instance describing the last publish
        @rtype:  datetime or None
        """
        pass

    def query(self):
        # Placeholder - jconnor to implement
        pass
