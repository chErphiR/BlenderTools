# Copyright Epic Games, Inc. All Rights Reserved.
import bpy
import os
import tempfile
from enum import Enum


class ToolInfo(Enum):
    NAME = 'ue2rigify'
    LABEL = 'UE to Rigify'


class Modes(Enum):
    SOURCE = 'Source'
    METARIG = 'Edit Metarig'
    FK_TO_SOURCE = 'FK to Source'
    SOURCE_TO_DEFORM = 'Source to Deform'
    CONTROL = 'Control'


class Collections:
    EXTRAS_COLLECTION_NAME = 'Extras'
    CONSTRAINTS_COLLECTION_NAME = 'Constraints'


class Nodes:
    BONE_TREE_NAME = 'Bone Remapping Nodes'
    NODE_SOCKET_NAME = 'Bone Node Socket'
    SOURCE_RIG_OBJECT_NAME = 'Source Rig Object'
    SOURCE_RIG_CATEGORY = 'Source Rig Bones'
    CONTROL_RIG_FK_CATEGORY = 'Control Rig FK Bones'
    CONTROL_RIG_DEFORM_CATEGORY = 'Control Rig Deform Bones'


class Template:
    @staticmethod
    def RIG_TEMPLATES_PATH():
        if bpy.app.version[0] < 4:
            return os.path.join(tempfile.gettempdir(), ToolInfo.NAME.value, 'resources', 'rig_templates', 'b3_6')
        else:
            return os.path.join(tempfile.gettempdir(), ToolInfo.NAME.value, 'resources', 'rig_templates', 'b4_0')

    DEFAULT_MALE_TEMPLATE = 'male_mannequin_Ue4'
    DEFAULT_FEMALE_TEMPLATE = 'female_mannequin_Ue4'


class Viewport:
    DISPLAY_SPHERE = 'display_sphere'


class Rigify:
    WIDGETS_COLLECTION_NAME = 'WGTS_rig'
    META_RIG_NAME = 'metarig'
    CONTROL_RIG_NAME = 'rig'
    RIG_UI_FILE_NAME = 'rig_ui.py'
    LEFT_TOKEN = '.L'
    RIGHT_TOKEN = '.R'
