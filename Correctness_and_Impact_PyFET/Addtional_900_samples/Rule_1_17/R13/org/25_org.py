# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2020-12-15 22:26
import hanlp
from hanlp.components.mtl.multi_task_learning import MultiTaskLearning
from hanlp.components.mtl.tasks.tok.tag_tok import TaggingTokenization

# 加载多任务模型
HanLP: MultiTaskLearning = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_SMALL_ZH)
# 获取分词任务（以tok开头的任务都是分词任务，以细分标准为例）
tok: TaggingTokenization = HanLP['tok/fine']

tok.dict_force = tok.dict_combine = None
print(f'不挂词典:\n{HanLP("商品和服务项目")["tok/fine"]}')

tok.dict_force = {'和服', '服务项目'}
print(f'强制模式:\n{HanLP("商品和服务项目")["tok/fine"]}')  # 慎用，详见《自然语言处理入门》第二章
