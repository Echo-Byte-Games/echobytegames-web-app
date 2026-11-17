/* Echo Byte Games — small enhancements for the static site. */

(function () {
  "use strict";

  const EMAIL = "echobytegames01@gmail.com";

  function pageKey(pathname) {
    const parts = pathname.split("/");
    let last = parts[parts.length - 1] || "index";
    last = last.replace(/\.html$/i, "");
    return last === "" ? "index" : last;
  }

  function initNav() {
    const toggle = document.querySelector(".nav-toggle");
    const links = document.querySelector(".nav-links");

    if (toggle && links) {
      toggle.addEventListener("click", function () {
        const open = toggle.getAttribute("aria-expanded") === "true";
        toggle.setAttribute("aria-expanded", String(!open));
        links.classList.toggle("is-open", !open);
      });

      links.addEventListener("click", function (event) {
        if (event.target.closest(".nav-link")) {
          toggle.setAttribute("aria-expanded", "false");
          links.classList.remove("is-open");
        }
      });

      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
          toggle.setAttribute("aria-expanded", "false");
          links.classList.remove("is-open");
        }
      });
    }

    const current = pageKey(window.location.pathname);
    document.querySelectorAll(".nav-link").forEach(function (link) {
      if (pageKey(link.pathname) === current) {
        link.classList.add("is-active");
        link.setAttribute("aria-current", "page");
      }
    });
  }

  function initYear() {
    const targets = document.querySelectorAll("[data-year]");
    if (targets.length) {
      const year = String(new Date().getFullYear());
      targets.forEach(function (el) {
        el.textContent = year;
      });
    }
  }

  function initReveal() {
    const items = document.querySelectorAll(".reveal");
    if (!items.length) return;

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: "0px 0px -40px 0px" }
    );

    items.forEach(function (el) {
      observer.observe(el);
    });
  }

  function initContactForm() {
    const form = document.getElementById("contact-form");
    if (!form) return;

    const status = document.getElementById("form-status");

    form.addEventListener("submit", function (event) {
      event.preventDefault();

      const name = form.elements["name"].value.trim();
      const from = form.elements["email"].value.trim();
      const subject = form.elements["subject"].value.trim() || "Website enquiry";
      const message = form.elements["message"].value.trim();

      if (!name || !from || !message) {
        if (status) {
          status.style.color = "var(--magenta)";
          status.textContent = "Please fill in your name, email and message.";
        }
        return;
      }

      const body =
        "From: " + name + "\n" +
        "Email: " + from + "\n\n" +
        message + "\n";

      const mailto =
        "mailto:" + EMAIL +
        "?subject=" + encodeURIComponent(subject) +
        "&body=" + encodeURIComponent(body);

      if (status) {
        status.style.color = "var(--green)";
        status.textContent = "Opening your email app… if nothing happens, email " + EMAIL + " directly.";
      }

      window.location.href = mailto;
    });
  }

  function initCopyEmail() {
    const button = document.getElementById("copy-email");
    if (!button) return;

    const status = document.getElementById("copy-status");

    function fallbackCopy(text) {
      const field = document.createElement("textarea");
      field.value = text;
      field.setAttribute("readonly", "");
      field.style.position = "absolute";
      field.style.left = "-9999px";
      document.body.appendChild(field);
      field.select();
      let ok = false;
      try {
        ok = document.execCommand("copy");
      } catch (err) {
        ok = false;
      }
      document.body.removeChild(field);
      return ok;
    }

    button.addEventListener("click", async function () {
      let ok = false;
      if (navigator.clipboard && window.isSecureContext) {
        try {
          await navigator.clipboard.writeText(EMAIL);
          ok = true;
        } catch (err) {
          ok = false;
        }
      }
      if (!ok) ok = fallbackCopy(EMAIL);

      if (status) {
        status.textContent = ok ? "Copied to clipboard!" : "Select and copy: " + EMAIL;
      }
      button.textContent = ok ? "COPIED!" : "COPY EMAIL";
      window.setTimeout(function () {
        button.textContent = "COPY EMAIL";
      }, 2200);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initNav();
    initYear();
    initReveal();
    initContactForm();
    initCopyEmail();
  });
})();
