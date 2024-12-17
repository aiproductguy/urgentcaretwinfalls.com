## .CursorRules
always start output with files-used in <context> brackets followed by the response

#R1
<div class="popup" id="myPopup">
  <div class="popup-content">
    <files-context>-><span class="close">&times;</span>
    <p>{files-used}</p>
  </div>
</div>

<style>
.popup {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.5);
}

.popup-content {
  background: #fff;
  margin: 15% auto;
  padding: 20px;
  width: 80%;
  max-width: 500px;
}
</style>

---
always include upfront the rules that you use in the response from .cursorrules
example: #R1, #R2


---
Draft 2 Website Feedback
use poetry to make a script at `scripts/website_feedback_agent.py` using browser_use package and looks at every page of https://urgentcaretwinfallscom.netlify.app and provides feedback on
1. Site Structure
2. Site Branding
3. Site Navigation
4. Site Content covers (Minor Injuries, Treating Illnesses, Physicals & Wellness Checkups, Diagnostic Services, X-rays & Imaging, Work-Related Medical)
5. Site Design
6. Onsite SEO

Draft 3 Comparison
use poetry to make a script at `scripts/compare_website_feedback.py` that references functions in `scripts/website_feedback_agent.py` and compares https://urgentcaretwinfallscom.netlify.app with localhost:3000 and provides feedback in .cache/{YYYYMMDD-HHMM}-compare.md


---
use pnpm to make a NUXT 3 app that uses tailwind at app/ in the project root dir that:
1. uses Website Feedback output at .cache/20241216-205807-feedback.md
2. improves that pages, header, footer, navigation, and design
3. deploy to netlify and run website_feedback_agent.py again for the new app
