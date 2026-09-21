(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var yearEl = document.getElementById("year");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  var pending = Array.prototype.slice.call(document.querySelectorAll(".reveal"));

  function revealAll() {
    pending.forEach(function (el) { el.classList.add("in"); });
    pending = [];
  }

  // a sweep also catches elements the viewport jumped past, which an observer never reports
  function sweepReveals() {
    if (!pending.length) return;
    var limit = window.innerHeight * 0.92;
    pending = pending.filter(function (el) {
      if (el.getBoundingClientRect().top < limit) {
        el.classList.add("in");
        return false;
      }
      return true;
    });
  }

  if (reduceMotion) revealAll();
  else sweepReveals();

  var nav = document.getElementById("nav");
  var progress = document.getElementById("navProgress");

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    nav.classList.toggle("is-stuck", y > 12);

    var doc = document.documentElement;
    var max = doc.scrollHeight - window.innerHeight;
    progress.style.width = (max > 0 ? (y / max) * 100 : 0) + "%";

    if (!reduceMotion) sweepReveals();
  }

  var ticking = false;
  window.addEventListener("scroll", function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () { onScroll(); ticking = false; });
  }, { passive: true });
  onScroll();

  // a background tab pauses rAF, which would leave `ticking` latched; re-sync on return
  document.addEventListener("visibilitychange", function () {
    if (!document.hidden) { ticking = false; onScroll(); }
  });

  // scroll-spy: highlight the current section and slide the pill behind it
  var navLinks = Array.prototype.slice.call(document.querySelectorAll(".nav__link"));
  var allNavAnchors = Array.prototype.slice.call(document.querySelectorAll("[data-nav]"));
  var pill = document.getElementById("navPill");

  var sections = allNavAnchors
    .map(function (a) { return document.querySelector(a.getAttribute("href")); })
    .filter(Boolean)
    .filter(function (el, i, arr) { return arr.indexOf(el) === i; });

  function movePill(link) {
    if (!pill || !link) return;
    pill.style.width = link.offsetWidth + "px";
    pill.style.transform = "translateX(" + link.offsetLeft + "px)";
    pill.classList.add("on");
  }

  function setActive(id) {
    navLinks.forEach(function (link) {
      var isMatch = link.getAttribute("href") === "#" + id;
      link.classList.toggle("is-active", isMatch);
      if (isMatch) movePill(link);
    });
  }

  if (sections.length && "IntersectionObserver" in window) {
    var visible = new Map();

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        visible.set(entry.target.id, entry.isIntersecting ? entry.intersectionRatio : 0);
      });

      var bestId = null, bestRatio = 0;
      visible.forEach(function (ratio, id) {
        if (ratio > bestRatio) { bestRatio = ratio; bestId = id; }
      });
      if (bestId) setActive(bestId);
    }, {
      rootMargin: "-" + (nav.offsetHeight + 10) + "px 0px -45% 0px",
      threshold: [0, 0.15, 0.35, 0.6, 0.9]
    });

    sections.forEach(function (section) { spy.observe(section); });
  }

  window.addEventListener("resize", function () {
    var active = document.querySelector(".nav__link.is-active");
    if (active) movePill(active);
    if (!reduceMotion) sweepReveals();
  });

  window.addEventListener("load", function () {
    if (!reduceMotion) sweepReveals();
  });

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () {
      var active = document.querySelector(".nav__link.is-active");
      if (active) movePill(active);
    });
  }

  var burger = document.getElementById("burger");
  var mobileMenu = document.getElementById("mobileMenu");

  function closeMenu() {
    burger.setAttribute("aria-expanded", "false");
    burger.setAttribute("aria-label", "Open menu");
    mobileMenu.hidden = true;
  }

  burger.addEventListener("click", function () {
    var open = burger.getAttribute("aria-expanded") === "true";
    if (open) {
      closeMenu();
    } else {
      burger.setAttribute("aria-expanded", "true");
      burger.setAttribute("aria-label", "Close menu");
      mobileMenu.hidden = false;
    }
  });

  mobileMenu.addEventListener("click", function (e) {
    if (e.target.tagName === "A") closeMenu();
  });

  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && burger.getAttribute("aria-expanded") === "true") {
      closeMenu();
      burger.focus();
    }
  });

  var swap = document.querySelector("[data-swap]");
  if (swap && !reduceMotion) {
    var words = swap.children.length;
    var i = 0;
    setInterval(function () {
      i = (i + 1) % words;
      swap.style.transform = "translateY(-" + (i * (100 / words)) + "%)";
    }, 2200);
  }
})();
