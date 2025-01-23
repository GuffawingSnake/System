<template>
  <page-background>
    <div class="home">
      <!-- 添加时钟组件 -->
      <digital-clock></digital-clock>

      <!-- 顶部标题区域 -->
      <div class="system-title">
        <div class="title-icon">
          <i class="el-icon-first-aid-kit"></i>
        </div>
        <h1>AI 智慧照护助手</h1>
        <p class="subtitle">专业的智能照护系统 · 科学的个性化解决方案</p>
        <div class="title-decoration">
          <span class="line"></span>
          <i class="el-icon-plus medical-plus"></i>
          <span class="line"></span>
        </div>
      </div>

      <!-- 主要功能区域 -->
      <el-row :gutter="30" class="main-features">
        <el-col :span="12">
          <el-card class="feature-card" shadow="hover">
            <div class="card-icon">
              <i class="el-icon-edit-outline"></i>
            </div>
            <div class="card-header">
              <h3>问题输入</h3>
              <span class="badge">问卷调查</span>
            </div>
            <div class="card-content">
              <p>通过问卷形式收集老年人照护需求和问题</p>
              <ul class="feature-list">
                <li><i class="el-icon-check"></i> 基础信息收集</li>
                <li><i class="el-icon-check"></i> 照护需求评估</li>
                <li><i class="el-icon-check"></i> 问题详细描述</li>
              </ul>
              <el-button type="primary" @click="$router.push('/survey')" class="action-button">
                <i class="el-icon-edit"></i>
                开始填写
              </el-button>
            </div>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card class="feature-card" shadow="hover">
            <div class="card-icon">
              <i class="el-icon-document"></i>
            </div>
            <div class="card-header">
              <h3>照护方案</h3>
              <span class="badge">AI定制</span>
            </div>
            <div class="card-content">
              <p>基于问卷信息生成个性化照护建议</p>
              <ul class="feature-list">
                <li><i class="el-icon-check"></i> 专业评估分析</li>
                <li><i class="el-icon-check"></i> 个性化建议</li>
                <li><i class="el-icon-check"></i> 解决方案推荐</li>
              </ul>
              <el-button type="success" @click="$router.push('/records')" class="action-button">
                <i class="el-icon-view"></i>
                查看方案
              </el-button>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <!-- 辅助功能区域 -->
      <el-row :gutter="30" class="secondary-features">
        <el-col :span="12">
          <el-card class="info-card" shadow="hover" @click.native="showCases">
            <div class="info-icon">
              <i class="el-icon-collection"></i>
            </div>
            <div class="info-content">
              <h4>典型案例</h4>
              <p>真实案例分析 · 经验分享</p>
            </div>
          </el-card>
        </el-col>
        <el-col :span="12">
          <el-card class="info-card" shadow="hover" @click.native="showFAQ">
            <div class="info-icon">
              <i class="el-icon-question"></i>
            </div>
            <div class="info-content">
              <h4>共性问题解答</h4>
              <p>常见问题 · 专业解答</p>
            </div>
          </el-card>
        </el-col>
      </el-row>

      <!-- 对话框部分 -->
      <el-dialog title="典型案例" :visible.sync="casesVisible" width="70%">
        <div class="cases-content">
          <el-collapse v-model="activeCase">
            <el-collapse-item title="过度照护的危害" name="1">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>张阿姨的老伴患有轻度认知障碍。由于过度担心，张阿姨事事都要亲力亲为：给老伴穿衣、喂饭、洗漱，甚至不让老伴自己上厕所。随着时间推移，老伴的自理能力明显下降，连简单的扣扣子都做不到了。这种情况不仅加重了张阿姨的照护负担，也让她感到更加焦虑。医生指出，过度照护反而加速了老人功能的退化，建议在确保安全的前提下，尽可能让老人保持独立生活的能力。张阿姨意识到自己的做法可能弊大于利，但又担心如果放手会发生意外。通过与社区康复师沟通，她逐渐学会了如何在照护和放手之间找到平衡，既保证老伴的安全，又能维持其自理能力。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>评估老人现有能力，列出他能独立完成的事项清单</li>
                  <li>循序渐进：先让老人完成简单的自理任务，如自己吃饭、简单的穿衣</li>
                  <li>给予适当指导和鼓励，而不是包办代替</li>
                  <li>保持耐心，即使老人做得慢也要给予足够时间</li>
                  <li>在旁边看护但不干预，增强老人的安全感和自信心</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="沟通障碍的突破" name="2">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>李爷爷因为阿尔茨海默病，经常说不出想要表达的词语，有时会因为沟通不畅而变得烦躁。家人也常常因为猜不透他的需求而感到无助。这种情况在早餐时尤为明显，李爷爷想要表达自己想吃什么，却总是词不达意，最后往往以发脾气告终。家人尝试过多种方法，但效果都不理想。后来在医生的建议下，家人制作了一本包含日常用品图片的交流本，包括食物、衣物、日用品等。同时，他们也开始更多地观察李爷爷的非语言表达，比如面部表情和手势。渐渐地，他们发现李爷爷在使用图片交流本时情绪明显平静许多，沟通效果也好了很多。特别是在固定作息后，李爷爷的语言表达能力在某些时段会比较好，家人也会选择在这些时候与他进行更多交流。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>使用图片卡片辅助沟通</li>
                  <li>保持简单清晰的语言表达</li>
                  <li>给予足够的时间让老人表达</li>
                  <li>观察肢体语言和表情</li>
                  <li>建立日常生活规律，减少沟通障碍</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="走失预防与处理" name="3">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>王大爷因认知障碍，经常独自外出后找不到回家的路。这种情况最初是从他偶尔在小区里迷路开始的，后来逐渐发展到在更远的地方走失。家人不得不把门反锁，但这样又影响了老人的心情和活动自由。有一次，王大爷趁家人不注意，独自出门去找多年前的老房子，结果在陌生的街道上徘徊了几个小时。幸运的是，他衣服上缝制的联系卡片帮助好心人联系到了家属。这次事件让家人意识到，单纯的限制并不是长久之计。通过社区医生的介绍，他们了解到多种防走失的辅助设备和方法。在采取相应措施后，王大爷既保持了一定的活动自由，家人也能及时知道他的位置，大大减少了走失的风险。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>为老人配戴GPS定位设备</li>
                  <li>在衣物上缝制联系信息</li>
                  <li>与社区和邻居建立联防网络</li>
                  <li>适当时候陪同外出，满足活动需求</li>
                  <li>在家中创造安全的活动空间</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="昼夜颠倒的调节" name="4">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>刘奶奶晚上总是睡不着，经常在家里走动，白天却总是犯困。这种情况从半年前开始逐渐加重，到现在几乎完全颠倒了作息。晚上不仅自己睡不着，还会到处开灯，翻找东西，有时还会开火做饭，这让家人非常担心安全问题。白天刘奶奶又总是昏昏欲睡，家人强行让她保持清醒，她就会变得烦躁不安。家人轮流照顾，但长期的睡眠不足让大家都身心疲惫。后来在老年科医生的指导下，家人开始系统地调整刘奶奶的作息。他们先是白天增加户外活动，控制午睡时间，晚上则营造安静舒适的睡眠环境。经过两个月的坚持，刘奶奶的睡眠逐渐规律起来，整个家庭的生活质量也得到了明显改善。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>白天增加适度的体力活动</li>
                  <li>控制午睡时间不超过30分钟</li>
                  <li>建立规律的作息时间表</li>
                  <li>睡前避免剧烈运动和兴奋性活动</li>
                  <li>调整室内光线，帮助分辨昼夜</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="进食困难的应对" name="5">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>陈爷爷因吞咽功能减退，经常发生呛咳，家人担心出现误吸，喂食时非常紧张。这个问题最初只是偶尔发生，但随着病情发展变得越来越频繁。特别是在喝水和吃流质食物时，呛咳情况更为严重。有一次，陈爷爷因为呛咳太厉害，出现了轻微的肺部感染，不得不住院治疗。这次经历让全家人都很受打击，开始害怕给老人进食。在医院期间，吞咽治疗师为他们做了专业指导，教会了家人如何调整食物形态，以及正确的喂食姿势和方法。同时，营养师也为陈爷爷制定了营养均衡又易于吞咽的膳食计划。通过这些专业指导和反复练习，陈爷爷的进食问题得到了很大改善，家人的信心也逐渐恢复。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>调整食物质地，选择软烂易咽的食物</li>
                  <li>使用增稠剂改善液体黏稠度</li>
                  <li>保持正确的进食姿势</li>
                  <li>细嚼慢咽，避免急躁</li>
                  <li>进食时保持愉悦的氛围</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="情绪波动的管理" name="6">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>赵阿姨的母亲常常无故发脾气，有时还会出现幻觉，指责家人偷她的东西，让家人既心疼又无奈。这种情况往往在傍晚时分最为明显，医生说这是典型的"日落综合征"。老人会坚持说自己的金项链不见了，指责保姆偷走了，尽管那条项链其实早在几年前就已经送给孙女了。有时还会说看到已故的老伴在房间里，要执意出门去找他。赵阿姨一开始总是试图讲道理，证明母亲的想法是错误的，结果反而让冲突升级。后来在老年精神科医生的指导下，他们学会了新的应对方式。比如不再直接否定老人的感受，而是先表示理解，然后巧妙地转移注意力。同时，他们也发现了一些诱发情绪波动的环境因素，如光线不足、环境嘈杂等，通过改善这些条件，老人的情绪问题得到了明显缓解。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>保持冷静，不与老人争辩</li>
                  <li>转移注意力到愉快的话题或活动</li>
                  <li>寻找情绪波动的潜在原因</li>
                  <li>创造安全舒适的环境</li>
                  <li>必要时寻求专业医生帮助</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="个人卫生的维护" name="7">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>钱奶奶拒绝洗澡和更换衣物，家人强行要求时就会发生冲突，导致双方关系紧张。这个问题在冬天尤为突出，钱奶奶总说"不冷不脏，不用洗"，一提到洗澡就很抗拒。家人发现她害怕浴室太冷，也担心滑倒，还有一些羞耻心。一次强行要求洗澡后，钱奶奶整整一周都不理家人。后来，家人在社区护士的建议下，先改善了浴室环境，安装了浴霸、防滑垫和扶手。同时，他们也学会了循序渐进的方法，先从每天擦手、洗脸开始，慢慢建立起清洁习惯。特别是发现钱奶奶喜欢在下午太阳暖和的时候活动，就选择在这个时间段提供帮助。经过耐心引导，钱奶奶开始逐渐接受定期的清洁护理。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>了解老人抗拒的具体原因</li>
                  <li>选择老人最舒适的时间段</li>
                  <li>准备合适的水温和环境</li>
                  <li>使用正面引导而不是强迫</li>
                  <li>建立固定的清洁习惯</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="认知训练的开展" name="8">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>孙爷爷记忆力明显下降，家人想帮助他进行认知训练，但不知道如何开展，担心训练变成压力。最初他们买了很多认知训练的书籍和玩具，但孙爷爷完全提不起兴趣，觉得那些都是小孩子玩的。家人也试过让他背诗、算数，结果适得其反，老人因为总是答不对而产生挫败感。后来，一位康复师建议从老人的兴趣爱好入手。原来孙爷爷年轻时是个摄影爱好者，于是家人开始带他整理老照片，让他回忆照片里的人和事。慢慢地，他们又加入了一些简单的手工活动和园艺，这些都是孙爷爷熟悉和感兴趣的。通过这种方式，认知训练变得自然而愉快，孙爷爷不仅积极参与，记忆力也有了明显改善。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>从简单的日常活动开始训练</li>
                  <li>使用老人熟悉的物品和话题</li>
                  <li>结合兴趣爱好设计活动</li>
                  <li>保持训练的趣味性和成就感</li>
                  <li>循序渐进，避免给予压力</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="社交活动的促进" name="9">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>周奶奶因认知障碍而变得不愿意与人交往，整天把自己关在房间里，家人担心她会越来越封闭。这种情况是从她在麻将馆打错几次麻将，被熟人笑话后开始的。周奶奶因为害怕出错，渐渐地开始推辞所有社交活动。连最好的老姐妹来访，她也借故不见。家人发现她经常一个人在房间里自言自语，情绪也变得低落。社工建议从最基础的家庭互动开始，先是让孙子陪她看看电视，聊聊天。然后邀请她最要好的一两个朋友来家里喝茶。社区中心还组织了一个专门针对认知障碍老人的小组活动，让周奶奶在相似的群体中重建信心。经过半年的努力，周奶奶重新找到了社交的乐趣，还在社区活动中交到了新朋友。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>从家庭成员互动开始</li>
                  <li>邀请老朋友小规模探访</li>
                  <li>参与社区适老化活动</li>
                  <li>保持适度的社交频率</li>
                  <li>创造轻松愉快的社交氛围</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="家庭照护的协调" name="10">
              <div class="case-detail">
                <h4>案例描述：</h4>
                <p>吴家照顾患病老人的责任全部落在大女儿身上，导致她身心俱疲，家庭关系也变得紧张。作为主要照护者，大女儿不仅要照顾父亲的日常起居，还要负责送医就诊、协调医疗护理等事务。她自己的工作和家庭生活都受到了严重影响，经常失眠、焦虑。其他兄弟姐妹虽然也想帮忙，但因为缺乏经验和具体分工，反而经常产生矛盾。这种情况持续了大半年，直到大女儿出现了严重的抑郁症状。在社工的帮助下，家庭召开了会议，制定了详细的轮值表，明确了每个成员的职责。他们还联系了专业的居家护理服务，分担一部分照护工作。通过建立家庭微信群，及时分享照护情况，使得照护工作更加透明和高效。半年后，大女儿的状态明显改善，家庭关系也重归和睦。</p>
                <h4>解决方案：</h4>
                <ul>
                  <li>制定家庭成员轮班表</li>
                  <li>明确每个人的职责分工</li>
                  <li>寻求专业照护支持</li>
                  <li>定期召开家庭会议沟通</li>
                  <li>关注主要照护者的身心健康</li>
                </ul>
              </div>
            </el-collapse-item>
          </el-collapse>
        </div>
      </el-dialog>

      <el-dialog title="共性问题解答" :visible.sync="faqVisible" width="70%">
        <div class="faq-content">
          <el-collapse v-model="activeFAQ">
            <el-collapse-item title="如何应对老人的固执行为？" name="1">
              <div class="faq-item">
                <div class="video-container">
                  <video controls>
                    <source src="/videos/stubborn-behavior.mp4" type="video/mp4">
                    您的浏览器不支持视频播放
                  </video>
                </div>
                <div class="text-content">
                  <h4>问题分析：</h4>
                  <p>认知障碍老人的固执行为往往源于对环境变化的不适应和安全感的缺失。</p>
                  <h4>解决建议：</h4>
                  <ul>
                    <li>理解固执背后的原因，可能是恐惧或不安全感</li>
                    <li>避免直接对抗，采用迂回方式化解</li>
                    <li>保持生活环境的稳定性</li>
                    <li>给予足够的耐心和理解</li>
                    <li>在安全前提下适当妥协</li>
                  </ul>
                </div>
              </div>
            </el-collapse-item>

            <el-collapse-item title="如何预防失智老人噎食？" name="2">
              <div class="faq-item">
                <div class="video-container">
                  <video controls>
                    <source src="/videos/choking-prevention.mp4" type="video/mp4">
                    您的浏览器不支持视频播放
                  </video>
                </div>
                <div class="text-content">
                  <h4>问题分析：</h4>
                  <p>失智老人容易出现吞咽功能障碍，加上进食时注意力不集中，增加了噎食风险。吞咽障碍不仅影响营养摄入，还可能导致误吸性肺炎，需要特别关注。</p>
                  <h4>预防措施：</h4>
                  <ul>
                    <li>调整食物形态：选择软烂、易咽的食物，避免干硬、黏稠或易碎的食物</li>
                    <li>保持正确姿势：进食时保持端正坐姿，略微前倾，避免平躺进食</li>
                    <li>控制进食速度：一口一口细嚼慢咽，确保充分咀嚼</li>
                    <li>避免分心：进食时避免说话、看电视等分散注意力的行为</li>
                    <li>适当使用增稠剂：对于液体类食物，可适当使用增稠剂调整稠度</li>
                  </ul>
                </div>
              </div>
            </el-collapse-item>

            <el-collapse-item title="居家环境有哪些危险因素需要注意？" name="3">
              <div class="faq-item">
                <h4>问题分析：</h4>
                <p>失智老人对环境的感知和判断能力下降，家居环境中的许多常见设施可能成为安全隐患。及时识别和改善这些危险因素，可以有效预防意外发生。</p>
                <h4>主要危险因素及改善建议：</h4>
                <ul>
                  <li>地面防滑：浴室、厨房等潮湿区域需铺设防滑垫，清除地面障碍物</li>
                  <li>照明条件：保证充足照明，设置夜灯，避免强光刺激和明暗交替</li>
                  <li>家具布局：保持通道畅通，避免尖角家具，设置适当扶手</li>
                  <li>电器安全：加装漏电保护，煤气设施需配备自动报警装置</li>
                  <li>药品管理：集中存放，明确标识，避免误服或漏服</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="认知症的早期征兆有哪些？" name="4">
              <div class="faq-item">
                <h4>问题分析：</h4>
                <p>认知症的早期症状往往较为隐匿，容易被误认为是正常衰老。及早发现这些征兆，可以争取最佳干预时机。</p>
                <h4>主要早期征兆：</h4>
                <ul>
                  <li>记忆力变化：反复询问同样的问题，经常找不到东西</li>
                  <li>语言能力：词不达意，说话内容前后矛盾</li>
                  <li>时空感知：熟悉环境中迷路，对时间概念模糊</li>
                  <li>判断力：处理日常事务能力下降，财务决策出现失误</li>
                  <li>情绪行为：性格改变，出现焦虑、抑郁或易怒情绪</li>
                </ul>
              </div>
            </el-collapse-item>

            <el-collapse-item title="认知症的药物治疗和非药物治疗如何选择？" name="5">
              <div class="faq-item">
                <h4>问题分析：</h4>
                <p>认知症的治疗需要药物和非药物治疗相结合，两种方式各有优势，需要根据病情和个体差异进行选择。</p>
                <h4>治疗方式比较：</h4>
                <ul>
                  <li>药物治疗：
                    <ul>
                      <li>优势：可以延缓认知功能衰退，改善症状</li>
                      <li>局限：可能有副作用，效果因人而异</li>
                      <li>适用：中重度认知障碍，症状明显影响生活</li>
                    </ul>
                  </li>
                  <li>非药物治疗：
                    <ul>
                      <li>优势：安全性高，可改善生活质量，促进社会参与</li>
                      <li>方式：认知训练、音乐治疗、园艺治疗、运动疗法等</li>
                      <li>适用：轻度认知障碍，预防和维持治疗</li>
                    </ul>
                  </li>
                  <li>建议：
                    <ul>
                      <li>早期以非药物治疗为主，预防和延缓症状</li>
                      <li>中期结合使用，药物控制症状，非药物维持功能</li>
                      <li>需要在专业医生指导下选择合适的治疗方案</li>
                    </ul>
                  </li>
                </ul>
              </div>
            </el-collapse-item>
          </el-collapse>
        </div>
      </el-dialog>
    </div>
  </page-background>
</template>

<script>
import DigitalClock from '@/components/DigitalClock.vue'
import PageBackground from '@/components/PageBackground.vue'

export default {
  name: 'Home',
  components: {
    DigitalClock,
    PageBackground
  },
  data() {
    return {
      casesVisible: false,
      faqVisible: false,
      activeCase: '1',
      activeFAQ: '1'
    }
  },
  methods: {
    showCases() {
      this.casesVisible = true
    },
    showFAQ() {
      this.faqVisible = true
    }
  }
}
</script>

<style scoped>
.home {
  min-height: 100vh;
}

.system-title {
  text-align: center;
  margin-bottom: 50px;
  padding: 30px 0;
}

.title-icon {
  font-size: 48px;
  color: #409EFF;
  margin-bottom: 20px;
}

.system-title h1 {
  color: #2c3e50;
  font-size: 36px;
  margin-bottom: 15px;
  font-weight: 600;
}

.subtitle {
  color: #606266;
  font-size: 18px;
  margin: 0;
  letter-spacing: 1px;
}

.main-features {
  margin-bottom: 40px;
}

.feature-card {
  height: 100%;
  padding: 20px;
}

.card-icon {
  font-size: 40px;
  color: #409EFF;
  margin-bottom: 20px;
  text-align: center;
}

.card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}

.badge {
  background: #ecf5ff;
  color: #409EFF;
  padding: 4px 12px;
  border-radius: 15px;
  font-size: 14px;
}

.feature-list {
  list-style: none;
  padding: 0;
  margin: 20px 0;
}

.feature-list li {
  margin: 10px 0;
  color: #606266;
}

.action-button {
  width: 100%;
  margin-top: 20px;
}

.info-card {
  display: flex;
  align-items: center;
  padding: 20px;
  cursor: pointer;
}

.info-icon {
  font-size: 30px;
  color: #409EFF;
  margin-right: 20px;
}

.secondary-features {
  margin-top: 30px;
}

.video-container {
  margin-bottom: 20px;
  width: 100%;
  max-width: 800px;
  margin: 0 auto 20px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
}

.video-container video {
  width: 100%;
  display: block;
}

.text-content {
  padding: 20px;
  background: #f5f7fa;
  border-radius: 8px;
}

.faq-item {
  padding: 20px;
}

.faq-item h4 {
  color: #409EFF;
  margin: 15px 0;
}

.faq-item p {
  color: #606266;
  line-height: 1.6;
}

.faq-item ul {
  padding-left: 20px;
}

.faq-item li {
  margin: 10px 0;
  color: #606266;
}
</style>
