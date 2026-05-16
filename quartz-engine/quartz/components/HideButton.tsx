import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"
// @ts-ignore
import script from "./scripts/hideReport.inline"

const WEBHOOK_URL = process.env.CONTENT_MODERATION_WEBHOOK || "http://127.0.0.1:8092/api/moderate"

const HideButton: QuartzComponent = ({ fileData, cfg }: QuartzComponentProps) => {
  const slug = fileData.slugPath ?? ""
  const title = fileData.frontmatter?.title ?? ""

  return (
    <div class={classNames("echo-hide-report")}>
      <button
        class="echo-hide-btn"
        data-slug={slug}
        data-title={title}
        data-webhook={WEBHOOK_URL}
        onclick="window.__echoHideReport(event)"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>
        </svg>
        Hide &amp; Report
      </button>
    </div>
  )
}

HideButton.afterDOMLoaded = script

export default (() => HideButton) satisfies QuartzComponentConstructor<{}>
