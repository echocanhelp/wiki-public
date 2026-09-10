#!/usr/bin/env bash
# echopedia-quote-extractor-all.sh — Run quote extractor for all TAHS members
# Runs daily at 04:15 after timeline builder
set -uo pipefail
[[ -f /tmp/pinto-cpu-freeze ]] && exit 0

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

PAR="$("$SCRIPT_DIR/echopedia-guard.sh" 2>/dev/null || echo 0)"
if ! [[ "$PAR" =~ ^[1-9][0-9]*$ ]]; then
    echo "=== Quote Extractor: skip (peak-hour/freeze par=${PAR:-0}) ==="
    exit 0
fi
export PYTHON SCRIPT_DIR
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
echo "=== Quote Extractor: All TAHS Members (par=$PAR) ==="
echo "Processing ${#SLUGS[@]} members..."

printf '%s\n' "${SLUGS[@]}" | xargs -P "$PAR" -I{} \
    $PYTHON "$SCRIPT_DIR/echopedia-quote-extractor.py" --person {}

echo "=== Done ==="
