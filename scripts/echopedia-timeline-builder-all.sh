#!/usr/bin/env bash
# echopedia-timeline-builder-all.sh — Run timeline builder for all TAHS members
# Runs daily at 04:00 after echopedia-scout-live
set -uo pipefail

SCRIPT_DIR="$HOME/echo-system/scripts"
PYTHON="python3"

# All TAHS member slugs with Chinese names
SLUGS=(
    alan-thian paul-chen yang-jia-you gene-tsai xu-shihuan linda-liu
    leonard-hsu-jr roger-tsai bai-weiwei john-yang yi-sen-lee
    phoenix-ko freeman-huang tzetsai-eric-shen sunu-tsai david-lee
    ken-wu rex-chen ashton-hsu albert-s-lai willy-pan franklin-ping-cheng
    chen-wenshi huang-gen-shen liao-shu-zong
    bai-peiyu cao-changqing zhang-xinhui chao-sile
    chen-bozhi chen-zhaonan chen-maoxiong chen-po-kong
    zheng-qinren zheng-wenlong jin-hegui du-ao-cunfu
    fan-jiang-ti-ang gong-sun-le he-qingxuan hu-ping
    huang-diyin huang-yongcheng guan-renjian li-xiaofeng
    li-jian liao-qingshan lin-baohua lin-rongsong
    nanfang-shuo sang-pu tang-peili zou-jingwen
    wang-qiaoling wang-dan wang-shufen wei-jingsheng
    wu-lipei xia-ming yang-yuanxun yang-yueqing
    yang-ziqing ye-siya yu-jie yuan-zhihui
    zheng-bingquan
)

echo "=== Timeline Builder: All TAHS Members ==="
echo "Processing ${#SLUGS[@]} members..."

for slug in "${SLUGS[@]}"; do
    $PYTHON "$SCRIPT_DIR/echopedia-timeline-builder.py" --person "$slug" 2>&1
done

echo "=== Done ==="
