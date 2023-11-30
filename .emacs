;; Melpa
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
;; Comment/uncomment this line to enable MELPA Stable if desired.  See `package-archive-priorities`
;; and `package-pinned-packages`. Most users will not need or want to do this.
;;(add-to-list 'package-archives '("melpa-stable" . "https://stable.melpa.org/packages/") t)
(package-initialize)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(blink-cursor-mode nil)
 '(column-number-mode t)
 '(custom-enabled-themes '(deeper-blue))
 '(fringe-mode 0 nil (fringe))
 '(package-selected-packages '(markdown-mode haskell-mode gap-mode sage-shell-mode))
 '(tool-bar-mode nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(default ((t (:family "Noto Sans Mono" :foundry "GOOG" :slant normal :weight normal :height 98 :width normal)))))

;; Disable the splash screen.
(setq inhibit-splash-screen t)

;; Window width and height.
(add-to-list 'default-frame-alist '(height . 57))
(add-to-list 'default-frame-alist '(width . 83))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Custom key binding.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Go to beginning of buffer.
(global-set-key (kbd "<f2>") 'beginning-of-buffer)

;; Go to end of buffer.
(global-set-key (kbd "<f3>") 'end-of-buffer)

;; Comment a region.
(global-set-key (kbd "<f4>") 'comment-region)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; Miscellaneous
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; Each line should be no more than 80 characters in length.  Use autofill for
;; all text mode buffers.
(setq-default auto-fill-function 'do-auto-fill)
(setq-default fill-column 80)

;; Remove trailing whitespace upon write.
(add-hook 'before-save-hook
          'delete-trailing-whitespace)

;; Untabify upon save.  Does not affect Makefile.
;; By https://stackoverflow.com/users/936762/dan From
;;
;; https://stackoverflow.com/a/24857101
(defun untabify-except-makefiles ()
  "Replace tabs with spaces except in Makefiles."
  (unless (derived-mode-p 'makefile-mode)
    (untabify (point-min) (point-max))))
(add-hook 'before-save-hook 'untabify-except-makefiles)

;; A final newline at the end of the file.
(setq require-final-newline t)
